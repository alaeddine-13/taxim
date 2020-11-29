from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager as BuiltinUserManager
from django.core.validators import RegexValidator
from phone_verify.models import SMSVerification
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.shortcuts import get_object_or_404
from .backends.storage_backends import PublicMediaStorage, PrivateMediaStorage

class UserManager(BuiltinUserManager):
    USERNAME_FIELD = 'phone_number'
    def create_superuser(self, email=None, password=None, **extra_fields):
        return super().create_superuser(
            extra_fields.get(self.USERNAME_FIELD),
            email=email,
            password=password,
            **extra_fields
        )
    
    def create_user(self, email=None, password=None, **extra_fields):
        return super().create_user(
            extra_fields.get(self.USERNAME_FIELD),
            email=email,
            password=password,
            **extra_fields
        )

class User(AbstractUser):
    phone_regex = RegexValidator(regex=r'^\+216\d{8}$', message="Phone number must be entered in the format: (+216)xxxxxxxx")
    phone_number = models.CharField(validators=[phone_regex], max_length=20, unique=True)
    phone_verified = models.BooleanField(default=False)
    credits = models.IntegerField(default=1000)
    image_url = models.CharField(max_length=255, null=True)
    objects = UserManager()
    USERNAME_FIELD = objects.USERNAME_FIELD

@receiver(post_save, sender=SMSVerification)
def verify_user(sender, instance=None, created=None, **kwargs):
    if not created and instance.is_verified:
        user = get_object_or_404(User.objects.filter(phone_number=instance.phone_number))
        user.phone_verified = True
        user.save()

class Upload(models.Model):
    uploaded_at = models.DateTimeField(auto_now_add=True)
    file = models.FileField(storage=PublicMediaStorage())


class UploadPrivate(models.Model):
    uploaded_at = models.DateTimeField(auto_now_add=True)
    file = models.FileField(storage=PrivateMediaStorage())
