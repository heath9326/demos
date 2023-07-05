from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from accounts.models import Person

class CreateUserForm(UserCreationForm):
    class Meta:
        model = Person
        fields = ['username', 'email', 'password1', 'password2']