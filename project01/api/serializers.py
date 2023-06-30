from rest_framework import serializers
from django.contrib.auth.models import User
from api.models import ToDo




class ToDoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ToDo
        fields = ['title', 'body']