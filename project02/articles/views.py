from django.shortcuts import render

# Project specific:
from .models import Article, Comment
from .serializers import ArticleSerializer, CommentSerializer


# REST
from rest_framework.response import Response
from rest_framework.views import APIView

class GetArticlesView(APIView):
    serializer_class = ArticleSerializer

    def get_queryset(self):
        authors = Article.objects.all()
        return authors

    def get(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = ArticleSerializer(instance=queryset, many=True)
        return Response(serializer.data)
    
    #TODO: def post()
    #TODO: def delete()
    #TODO: def put()
    #TODO: def patch()

class GetCommentsView(APIView):
    serializer_class = CommentSerializer

    def get_queryset(self):
        authors = Comment.objects.all()
        return authors
    
    def get(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = CommentSerializer(instance=queryset, many=True)
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

#TODO: class ListAPIViewArticlesSingle(drf_generics.ListAPIViewAPIView):

#TODO: class RetrieveAPIViewArticlesSingle(drf_generics.RetrieveAPIView):

#TODO: class DestroyAPIViewArticlesSingle(drf_generics.DestroyAPIView):

#TODO: class UpdateAPIViewArticlesSingle(drf_generics.DestroyAPIView):

#TODO: class ListCreateArticlesSingle(drf_generics.ListCreateAPIView):

#TODO: class RetrieveUpdateArticlesSingle(drf_generics.RetrieveUpdateAPIView):   

#TODO: class RetrieveDestroyArticlesSingle(drf_generics.RetrieveDestroyAPIView):

#TODO: class RetrieveUpdateDestroyArticlesSingle(drf_generics.RetrieveUpdateDestroyAPIView):