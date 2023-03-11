from django.db.models.signals import post_save
from django.dispatch import receiver

# Models
# from django.contrib.auth.models import User
from accounts.models import User
from accounts.models import Profile
from accounts.models import Address

# To automatically create profile for user


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, *args, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_profile(sender, instance, *args, **kwargs):
    instance.profile.save()


@receiver(post_save, sender=User)
def create_present_address(sender, instance, created, *args, **kwargs):
    if created:
        Address.objects.create(address_of=instance)


@receiver(post_save, sender=User)
def save_present_address(sender, instance, *args, **kwargs):
    instance.address.save()
