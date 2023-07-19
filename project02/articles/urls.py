from django.urls import path

# Imports
from .views import GetArticlesView, GetCommentsView


app_name = 'articles'

urlpatterns = [
    path('getarticlesapi', GetArticlesView.as_view(), name='getarticlesapi'),
    path('getcommentsapi', GetCommentsView.as_view(), name='getcommentsapi'),
]