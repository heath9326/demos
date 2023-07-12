from rest_framework import serializers

from .models import CustomUser

class CustomUserSerializer(serializers.ModelSerializer):

    def create(self, validated_data):

        user = CustomUser.objects.create_user(
            username=validated_data['username'],
            email = validated_data['email'],
            password=validated_data['password'],
        )
        return user    

    class Meta:
        model = CustomUser
        fields = '__all__'