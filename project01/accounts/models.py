from django.db import models
from django.contrib.auth.admin import User
# Create your models here.

class Person(User):

    class Meta:
        proxy = True
