from django.shortcuts import render

# Project specific:
from .models import Article
from .serializers import ArticleSerializer


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
