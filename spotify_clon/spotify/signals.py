from .models import User
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.contrib.auth.hashers import make_password #, check_password
#HASH PASSWORD:
@receiver(pre_save, sender=User)
def hash_user_password(sender, instance, **kwargs):
    if instance.password and not instance.password.startswith('pbkdf2_sha256$'):
        instance.password = make_password(instance.password)
    