from rest_framework import serializers

from accounts.models import Person


class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        # Works with API view if only username is selected and doesn't if all are. Oooooops does not work at all anymore
        fields = '__all__'