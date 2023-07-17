from django.urls import path

# Imports
from .views import GetAuthorsView


app_name = 'authors'

urlpatterns = [
    path('getautorsapi', GetAuthorsView.as_view(), name='getautorsapi'),
]