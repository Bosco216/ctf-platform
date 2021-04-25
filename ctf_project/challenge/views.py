from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (
    ListView, 
    DetailView, 
    CreateView,
    UpdateView,
    DeleteView
)
from django.contrib.auth.decorators import login_required
from .models import Challenge, Competition, User, Team
import datetime
from .forms import SubmitFlagForm
from django.contrib import messages
# Create your views here.

# Scoreboard
class ScoreBoardView(UserPassesTestMixin, ListView):
    model = Team
    template_name = 'challenge/scoreboard.html'
    context_object_name = 'Teams'
    ordering = ['-score']

    # make sure current user is login
    def test_func(self):
        if self.request.user in User.objects.all():
            return True
        else: 
            return False

# Check if the user is Superuser(admin)
class AdminRequiredMixin(LoginRequiredMixin, UserPassesTestMixin):
    
    def test_func(self):
        return self.request.user.is_superuser

# Competition View
class CompetitionListView(AdminRequiredMixin, ListView):
    model = Competition
    template_name = 'challenge/list_comp.html' # <app>/<model>_<viewtype>.html
    context_object_name = 'competitions'

class CompetitionCreateView(AdminRequiredMixin, CreateView):
    model = Competition
    fields = ['name', 'start_time', 'end_time']

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)

class CompetitionUpdateView(AdminRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Competition
    fields = ['name', 'start_time', 'end_time']

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)

    # make sure current user is the owner of the current Competition that want to update
    def test_func(self):
        competition = self.get_object()
        if self.request.user == competition.owner:
            return True
        else: 
            return False

class CompetitionDeleteView(AdminRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Competition
    success_url = '/'
    
    def test_func(self):
        competition = self.get_object()
        if self.request.user == competition.owner:
            return True
        else: 
            return False

# Team can view the Challenge while competition is starting
@login_required
def Comp_Started_Team_ChallengeView(request):

    current_time = datetime.datetime.now()
    context = {
        'Teams': Team.objects.all(),
        'challenges': Challenge.objects.all().order_by('score'),
        'competitions': Competition.objects.all(),
        'current_time': current_time,
    }
    
    return render(request, 'challenge/list_chall_comp_started.html', context)

# Challenge View
class ChallengeListView(AdminRequiredMixin, ListView):
    model = Challenge
    template_name = 'challenge/list.html' # <app>/<model>_<viewtype>.html
    context_object_name = 'challenges'
    ordering = ['score']

class ChallengeDetailView(DetailView):
    model = Challenge

class ChallengeCreateView(AdminRequiredMixin, CreateView):
    model = Challenge
    fields = ['name', 'content', 'category', 'score', 'flag', 'file']

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)

class ChallengeUpdateView(AdminRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Challenge
    fields = ['name', 'content', 'category', 'score', 'flag', 'file']

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)

    # make sure current user is the owner of the current challenge that want to update
    def test_func(self):
        challenge = self.get_object()
        if self.request.user == challenge.owner:
            return True
        else: 
            return False

class ChallengeDeleteView(AdminRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Challenge
    success_url = '/'
    
    def test_func(self):
        challenge = self.get_object()
        if self.request.user == challenge.owner:
            return True
        else: 
            return False

# submit flag
@login_required
def submitFlag(request, pk):
    # pk: current challenge id
    # counter : store the score if flag is correct 
    c_score = 0
    if request.method == 'POST':
        submitFlag_form = SubmitFlagForm(request.POST, instance=request.user.team)
        if submitFlag_form.is_valid():
            for challenge in Challenge.objects.all():
                # check if challenge id are same
                if challenge.pk == pk:
                    # get input flag by name of input_flag in the form data
                    # check flag
                    if challenge.flag ==  request.POST.get('input_flag'):
                        c_score = challenge.score
                        # add score for correct flag and add to isSolved
                        for team in  Team.objects.all():
                            if team.user == request.user:
                                # check if the challenge has been solved
                                for solved_problem in team.solved_problems:
                                    if solved_problem == '99999999999999999999999999':
                                        team.solved_problems.remove('99999999999999999999999999')
                                        Team.save(team, update_fields=['solved_problems'])
                                for solved_problem in team.solved_problems:
                                    if challenge.name == solved_problem:
                                            messages.warning(request, f'You already sloved the problem!')
                                            return redirect('comp-start-view-challenge')

                                team.score += c_score
                                team.solved_problems.append(challenge.name)
                                # save the result to database: Team Score
                                Team.save(team, update_fields=['score', 'solved_problems'])
                                messages.success(request, f'You get the flag! Team score was successfully updated!')
                                return redirect('comp-start-view-challenge')
                    else:
                        messages.warning(request, f'The input flag is wrong!')
                
        else:
            messages.error(request, 'There are some errors!')

    else:
        submitFlag_form = SubmitFlagForm(request.POST, instance=request.user.team)

    context = {
        'submitFlag_form': submitFlag_form
    }

    return render(request, 'challenge/submit_challenge.html', context)