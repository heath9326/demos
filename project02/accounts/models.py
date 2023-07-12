from django.db import models
from django.contrib.auth.base_user import BaseUserManager

from django.contrib.auth.models import AbstractUser
from .managers import CustomUserManager

class CustomUser(AbstractUser):
    email = models.EmailField('email', unique=True)

    objects = CustomUserManager()

    def __str__(self):
        return f'CustomUser [{self.username}]: <{self.email}>'
    

