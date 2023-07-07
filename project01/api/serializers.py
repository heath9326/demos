from rest_framework import serializers

from api.models import ToDo
from accounts.models import Person


class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = '__all__'


class ToDoSerializer(serializers.ModelSerializer):
    #Возвращает ValueKey Error
    user = PersonSerializer(many=False, read_only=True)
    
    #Не возвращает ничего
    #user = PersonSerializer

    # Константа работает
    #user = serializers.ReadOnlyField(default='User01')
    class Meta:
        model = ToDo
        fields = ['id', 'title', 'body', 'user',]