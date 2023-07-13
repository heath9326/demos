from django.urls import path

# Imports
from .views import GetCustomUsersView, CustomUserListAPIView, SingleUserRetrieveView, get_users, test


app_name = 'accounts'

urlpatterns = [
    path('getusersapi', GetCustomUsersView.as_view(), name='getusersapi'),
    path('getuserapi/<int:pk>', GetCustomUsersView.as_view(), name='getusersapi'),
    path('getusersdecorator', get_users, name='getusersdecorator'),
    path('getuserslist', CustomUserListAPIView.as_view(),name='getuserslist'),
    path('getsingleuser/<int:pk>', SingleUserRetrieveView.as_view(), name='getsingleuser'),
    path('test/<int:pk>/', test, name='test'),
    # path('testkwargs', testkwargs, name='testkwargs'),
]
