from rest_framework import serializers
from api.models import ToDo

from accounts.models import Person


class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = '__all__'


class ToDoSerializer(serializers.ModelSerializer):
    # user = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = ToDo
        fields = ['id', 'title', 'user']