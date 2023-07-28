from django.urls import path

# Imports
from .views import ArticlesViewAPI, GetCommentsView


app_name = 'articles'

urlpatterns = [
    path('articlesviewapi', ArticlesViewAPI.as_view(), name='articlesviewapi'),
    path('getcommentsapi', GetCommentsView.as_view(), name='getcommentsapi'),
]