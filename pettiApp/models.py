from django.db import models
from django.contrib.auth.models import AbstractUser
from pettiApp.managers import UserManager


class User(AbstractUser):
    email = models.EmailField(unique=True)
    username = models.CharField(
        max_length=150,
        null=True,
        blank=True,
       
    )
    is_administrator = models.BooleanField(default=False)
    is_partner = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
