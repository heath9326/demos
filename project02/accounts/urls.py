from django.urls import path

# Imports
from .views import GetCustomUsersView, CustomUserListAPIView, SingleUserRetrieveView, DeleteCustomUserView, DestroyCustomUserView, UpdateCustomUserSingle, ListCreateCustomUserSingle, RetrieveUpdateCustomUserSingle, RetrieveDestroyCustomUserSingle, RetrieveUpdateDestroyCustomUserSingle, get_users_decorator, test, testkwargs


app_name = 'accounts'

urlpatterns = [
    path('getusersapi', GetCustomUsersView.as_view(), name='getusersapi'),
    path('deleteusersapi/<int:pk>', DeleteCustomUserView.as_view(), name='deleteuserssapi'),
    path('getusersdecorator', get_users_decorator, name='getusersdecorator'),
    path('getuserslist', CustomUserListAPIView.as_view(),name='getuserslist'),
    path('getsingleuser/<int:pk>', SingleUserRetrieveView.as_view(), name='getsingleuser'),
    path('destroysingleuser/<int:pk>', DestroyCustomUserView.as_view(), name='destroysingleuser'),
    path('updatesingleuser/<int:pk>', UpdateCustomUserSingle.as_view(), name='updatesingleuser'),
    path('listcreateusers', ListCreateCustomUserSingle.as_view(), name='listcreateusers'),
    path('retrieveupdatesingleuser/<username>', RetrieveUpdateCustomUserSingle.as_view(), name='retrieveupdatesingleuser'),
    path('retrievedestroysingleuser/<email>', RetrieveDestroyCustomUserSingle.as_view(), name='retrievedestroysingleuser'),
    path('retrievedestroyupdatesingleuser/<email>', RetrieveUpdateDestroyCustomUserSingle.as_view(), name='retrievedestroyupdatesingleuser'),
    path('test/<int:pk>/', test, name='test'),
    path('testkwargs/', testkwargs, name='testkwargs'),
]
