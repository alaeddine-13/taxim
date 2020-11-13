from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator

class User(AbstractUser):
    phone_regex = RegexValidator(regex=r'^\(\+216\)\d{8}$', message="Phone number must be entered in the format: +216xxxxxxxx")
    phone_number = models.CharField(validators=[phone_regex], max_length=20, unique=True)
    credits = models.IntegerField(default=1000)
    image_url = models.CharField(max_length=255, null=True)
    USERNAME_FIELD = 'phone_number'
