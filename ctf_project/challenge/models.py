from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from django_mysql.models import ListTextField
# Create your models here.

# Competition Model
class Competition(models.Model):

    name = models.CharField(max_length=100)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()

    # ensure only can create one competition at once
    def save(self, *args, **kwargs):
        if self.__class__.objects.count():
            self.pk = self.__class__.objects.first().pk
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

# Challenge Model
class Challenge(models.Model):

    class Catergory(models.TextChoices):
        Web = 'Web', _('Web')
        Cryptography = 'Cryptography', _('Cryptography')
        Forensics = 'Forensics', _('Forensics')
        Reverse = 'Reverse', _('Reverse')
        Exploitation = 'Exploitation', _('Exploitation')
        Miscellaneous = 'Miscellaneous', _('Miscellaneous')

    name = models.CharField(max_length=200, unique=True)
    content = models.TextField()
    file = models.FileField(null=True, blank=True, upload_to='challenge_files')
    category = models.CharField(max_length=20, choices=Catergory.choices)
    score = models.IntegerField()
    flag = models.CharField(max_length=200)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    #### need to find a way to count solved team #######
    # solved_team = models.ForeignKey(User, on_delete=models.CASCADE)
    #### need to find a way to count solved team #######
    def __str__(self):
        return "Challenge" + self.name

    def get_absolute_url(self):
        return reverse('challenge-detail', kwargs={'pk': self.pk}) # return the full path as a string

class Team(models.Model):
    #user score and submit flag
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    score = models.IntegerField(blank=True, default=0)
    solved_problems = ListTextField(
        base_field=models.CharField(max_length=100),
        size=100, null=True, blank=True, default='99999999999999999999999999'  # Maximum of 100 challenges id in list
    )

    def __str__(self):
        # return "Team score" + str(self.team_score)
        return "User :" + str(self.user)

    def save(self,  *args, **kwargs):
        super(Team, self).save( *args, **kwargs)