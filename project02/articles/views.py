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
from django.core.exceptions import ObjectDoesNotExist
from rest_framework.renderers import (
                                        HTMLFormRenderer, 
                                        JSONRenderer, 
                                        BrowsableAPIRenderer,
                                    )


class ArticlesViewAPI(APIView):
    serializer_class = ArticleSetSerializer
    renderer_classes = (BrowsableAPIRenderer, JSONRenderer, HTMLFormRenderer)

    def get_queryset(self):
        articles = Article.objects.all()
        return articles

    def get(self, request, *args, **kwargs):
        try:
            id = request.query_params['id']
            if id != None:
                article = Article.objects.get(id=id)
                print(article)
                serializer = ArticleGetSerializer(article)
            else:
                return Response("Please input an id parameter.")
        except ObjectDoesNotExist:
            return Response("Article with this id does not exist.")
        except:
            queryset = self.get_queryset()
            serializer = ArticleGetSerializer(instance=queryset, many=True)

        return Response(serializer.data)
    
    def post(self, request):
        serializer = ArticleSetSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=400)

    def patch(self, request, *args, **kwargs):
        id = request.query_params["id"]
        article_object = Article.objects.get(id=id)
        serializer = ArticleSetSerializer(article_object, data=request.data, partial=True)
        if serializer.is_valid():
            # serializer.update(article_object, request.data)
            # или
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=400)

    #TODO: def delete()
    #TODO: def put()


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

#TODO: class ArticleModelView(viewsets.ModelViewSet):

    # def get_serializer_class(self):
    # if self.request.method == 'GET':
    #     return ArticleGetSerializer
    # else:
    #     return ArticleSetSerializer