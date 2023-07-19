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

    #TODO: def post()
    #TODO: def delete()
    #TODO: def put()
    #TODO: def patch()

#TODO: "@api_view":
    #TODO: request.method == 'GET':
    #TODO: request.method == 'POST':
    #TODO: request.method == 'DELETE':
    #TODO: request.method == 'PUT':
    #TODO: request.method == 'PUT':
    #TODO: request.method == 'PATCH':

#TODO: class ListAPIViewAuthorsSingle(drf_generics.ListAPIViewAPIView):

#TODO: class RetrieveAPIViewAuthorsSingle(drf_generics.RetrieveAPIView):

#TODO: class DestroyAPIViewAuthorsSingle(drf_generics.DestroyAPIView):

#TODO: class UpdateAPIViewAuthorsSingle(drf_generics.DestroyAPIView):

#TODO: class ListCreateAuthorsSingle(drf_generics.ListCreateAPIView):

#TODO: class RetrieveUpdateAuthorsSingle(drf_generics.RetrieveUpdateAPIView):   

#TODO: class RetrieveDestroyAuthorsSingle(drf_generics.RetrieveDestroyAPIView):

#TODO: class RetrieveUpdateDestroyAuthorsSingle(drf_generics.RetrieveUpdateDestroyAPIView):