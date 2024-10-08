from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    is_administrator = models.BooleanField(default=False)
    is_partner = models.BooleanField(default=False)