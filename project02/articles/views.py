from django.shortcuts import render

# Project specific:
from .models import Article, Comment
from .serializers import (
                            ArticleGetSerializer, 
                            ArticleSetSerializer, 
                            CommentSerializer
                        )



# REST
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.renderers import (
                                        HTMLFormRenderer, 
                                        JSONRenderer, 
                                        BrowsableAPIRenderer,
                                    )


class ArticlesViewAPI(APIView):
    serializer_class = ArticleSetSerializer
    renderer_classes = (BrowsableAPIRenderer, JSONRenderer, HTMLFormRenderer)

    def get_serializer_class(self):
        if self.request.method == 'GET':
           return ArticleGetSerializer
        else:
            return ArticleSetSerializer

    def get_queryset(self):
        authors = Article.objects.all()
        return authors

    def get(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer_class = self.get_serializer_class()
        serializer = serializer_class(instance=queryset, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer_class = self.get_serializer_class()
        serializer = serializer_class(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=400)

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

