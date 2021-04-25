from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (
    ListView, 
    DetailView, 
    CreateView,
    UpdateView,
    DeleteView
)
from .models import Notice
# Create your views here.

class NoticeListView(ListView):
    model = Notice
    template_name = 'notice/home.html' # <app>/<model>_<viewtype>.html
    context_object_name = 'notices'
    ordering = ['-datetime_created']

class NoticeDetailView(DetailView):
    model = Notice

class NoticeCreateView(LoginRequiredMixin, CreateView):
    model = Notice
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)

class NoticeUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Notice
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)

    # make sure current user is the owner of the current notice that want to update
    def test_func(self):
        notice = self.get_object()
        if self.request.user == notice.owner:
            return True
        else: 
            return False

class NoticeDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Notice
    success_url = '/'
    
    def test_func(self):
        notice = self.get_object()
        if self.request.user == notice.owner:
            return True
        else: 
            return False
    
def contact(request):
    return render(request, 'notice/contact.html', {'title': 'Contact'})