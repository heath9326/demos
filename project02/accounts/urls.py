from django.urls import path

# Imports
from .views import GetCustomUsersView

app_name = 'accounts'

urlpatterns = [
    path('getusers', GetCustomUsersView.as_view(), name='getusers'),
]
