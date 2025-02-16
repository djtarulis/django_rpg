from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings  # Import settings instead of the User model directly
from .models import Player
from django.contrib.auth.models import User

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_player_profile(sender, instance, created, **kwargs):
    if created:
        Player.objects.create(user=instance, name=instance.username)