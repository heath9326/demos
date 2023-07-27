from django.db import models

from django.contrib.auth.models import AbstractUser
from .managers import CustomUserManager

class CustomUser(AbstractUser):
    email = models.EmailField('email', unique=True)

    objects = CustomUserManager()

    def __str__(self):
        return f'CustomUser [{self.username}]: <{self.email}>'
    
    def make_inactive(self):
        self.is_active = False
        self.save()

    #FIXME: переопределить update method так что если в кваргах есть пассворт использовать set_password() вместо user["password"] = data["password"] 
