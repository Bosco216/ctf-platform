from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
# Create your models here.

# Notice Model
class Notice(models.Model):

    title = models.CharField(max_length=100)
    content = models.TextField()
    datetime_created = models.DateTimeField(default=timezone.now)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('notice-detail', kwargs={'pk': self.pk}) # return the full path as a string