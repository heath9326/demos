from django.urls import path

# Imports
from .views import GetArticlesView


app_name = 'authors'

urlpatterns = [
    path('getarticlesapi', GetArticlesView.as_view(), name='getarticlesapi'),
]