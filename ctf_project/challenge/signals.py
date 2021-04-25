from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Team

@receiver(post_save, sender=User)
def make_Team(sender, instance, created, **kwargs):
    if created:
        Team.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_Team(sender, instance, **kwargs):
    instance.team.save()