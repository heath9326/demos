from rest_framework import serializers

from api.models import ToDo
from accounts.models import Person


class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = ['username']


class ToDoSerializer(serializers.ModelSerializer):

    # Both options are the same in the ListCreateViewAPI, in API view
    # Gives a field and not a DICT is what I want but the serializer is still looking for the dick
    user = serializers.SlugRelatedField(
           queryset=Person.objects.all(), slug_field='username'
    )

    #Возвращает ValueKey Error
    # user = PersonSerializer(many=False, read_only=True)
    
    #Не возвращает ничего
    #user = PersonSerializer

    # Константа работает
    #user = serializers.ReadOnlyField(default='User01')
    class Meta:
        model = ToDo
        fields = ['id', 'title', 'body', 'user',]
        lookup_field = 'user'