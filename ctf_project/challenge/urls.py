from django.urls import path
from .views import (
    ChallengeListView,
    ChallengeDetailView,
    ChallengeCreateView,
    ChallengeUpdateView,
    ChallengeDeleteView,
    CompetitionListView,
    CompetitionCreateView,
    CompetitionUpdateView,
    CompetitionDeleteView, 
    ScoreBoardView
)
from . import views

urlpatterns = [
    #challenge path
    path('', ChallengeListView.as_view(), name='challenge-list'),
    path('<int:pk>/', ChallengeDetailView.as_view(), name='challenge-detail'),
    # create and update use the same template (challenge_form.html)
    path('create/', ChallengeCreateView.as_view(), name='challenge-create'),
    path('update/<int:pk>/', ChallengeUpdateView.as_view(), name='challenge-update'),
    # delete use challenge_confirm_delete.html for its template
    path('delete/<int:pk>/', ChallengeDeleteView.as_view(), name='challenge-delete'),
    # view Challenge when competition started
    path('competition_started_view_challenge/', views.Comp_Started_Team_ChallengeView, name='comp-start-view-challenge'),
    # submit challenge
    path('submit-challenge/<int:pk>/', views.submitFlag, name="submit-flag"),
    #competition path
    path('competition/', CompetitionListView.as_view(), name='competition-list'),
    # create and update use the same template (Competition_form.html)
    path('competition/create/', CompetitionCreateView.as_view(), name='competition-create'),
    path('competition/update/<int:pk>/', CompetitionUpdateView.as_view(), name='competition-update'),
    # delete use Competition_confirm_delete.html for its template
    path('competition/delete/<int:pk>/', CompetitionDeleteView.as_view(), name='competition-delete'),

    #scoreboard
    path('scoreboard/', ScoreBoardView.as_view(), name="scoreboard"),
]