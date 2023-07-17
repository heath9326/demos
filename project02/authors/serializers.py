from rest_framework import serializers

from .models import Author
from accounts.serializers import CustomUserSerializer

class AuthorSerializer(serializers.ModelSerializer):
    # Requred = False because Author can have and Author profile 
    # to be linked to the article without being a registered user:
    user = CustomUserSerializer(required=False)

    class Meta:
        model = Author
        fields = "__all__"

    def create(self, validated_data):
        user = CustomUserSerializer.create(CustomUserSerializer(), validated_data)
        author, created = Author.objects.create(user=user)
        return author