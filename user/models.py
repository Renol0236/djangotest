from django.contrib.auth.models import AbstractUser
from django.db import models


class Role(models.TextChoices):
    ADMIN = 'admin', 'Admin'
    USER = 'user', 'User'


class UserProfile(AbstractUser):
    role = models.CharField(max_length=5, choices=Role.choices, default=Role.USER)
