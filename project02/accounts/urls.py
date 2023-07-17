from django.urls import path

# Imports
from .views import GetCustomUsersView, CustomUserListAPIView, SingleUserRetrieveView, DeleteCustomUserView, DestroyCustomUserView, UpdateCustomUserSingle, get_users_decorator, test


app_name = 'accounts'

urlpatterns = [
    path('getusersapi', GetCustomUsersView.as_view(), name='getusersapi'),
    path('deleteusersapi/<int:pk>', DeleteCustomUserView.as_view(), name='deleteuserssapi'),
    path('getusersdecorator', get_users_decorator, name='getusersdecorator'),
    path('getuserslist', CustomUserListAPIView.as_view(),name='getuserslist'),
    path('getsingleuser/<int:pk>', SingleUserRetrieveView.as_view(), name='getsingleuser'),
    path('destroysingleuser/<int:pk>', DestroyCustomUserView.as_view(), name='destroysingleuser'),
    path('updatesingleuser/<int:pk>', UpdateCustomUserSingle.as_view(), name='updatesingleuser'),
    path('test/<int:pk>/', test, name='test'),
    # path('testkwargs', testkwargs, name='testkwargs'),
]
