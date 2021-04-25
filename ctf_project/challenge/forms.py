from django import forms
from django.contrib.auth.models import User
from .models import Team


class SubmitFlagForm(forms.ModelForm):

    class Meta:
        model = Team
        fields = ['score', 'solved_problems']