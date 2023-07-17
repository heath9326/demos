from django.shortcuts import render

# Project specific:
from .models import Author
from .serializers import AuthorSerializer

# REST
from rest_framework.response import Response
from rest_framework.views import APIView

class GetAuthorsView(APIView):
    serializer_class = AuthorSerializer

    def get_queryset(self):
        authors = Author.objects.all()
        return authors

    def get(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = AuthorSerializer(instance=queryset, many=True)
        return Response(serializer.data)