from django import forms

# Imports
from .models import ToDo


class CreateToDo(forms.ModelForm):
    class Meta:
        model = ToDo
        fields = ["body"]


class UpdateToDo(forms.Form):
    class Meta:
        model = ToDo
        fields = "__all__"
