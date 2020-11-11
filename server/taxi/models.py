from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    credits = models.IntegerField(default=1000)
    image_url = models.CharField(max_length=255, null=True)
