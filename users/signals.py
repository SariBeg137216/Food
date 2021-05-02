from django.db.models.signals import post_save
from django.contrib.auth.models import User
from .models import Profile
from django.dispatch import receiver


def profile_create(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


post_save.connect(profile_create, sender=User)


@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()





