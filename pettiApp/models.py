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
    description = models.TextField(null=True, blank=True)
    phone_number = models.CharField(max_length=15, null=True, blank=True)
    address = models.CharField(max_length=150, null=True, blank=True)
    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

class Service(models.Model):
    GROOMING = 'grooming'
    WALKING = 'walking'
    SITTING = 'sitting'
    SERVICE_TYPE_CHOICES = (
        (GROOMING, 'peluqueria'),
        (WALKING, 'paseo'),
        (SITTING, 'cuidado'),
    )
    service_type = models.CharField(
        choices=SERVICE_TYPE_CHOICES,
        default=GROOMING,
        max_length=30
    )

    price = models.IntegerField()
    partner = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='services'
    )

    def __str__(self):
        return self.service_type
