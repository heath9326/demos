from django.urls import path, include
# import routers
from rest_framework import routers

# Imports
from .views import (GetCustomUsersView, 
                    CustomUserListAPIView, 
                    SingleUserRetrieveView, 
                    DeleteCustomUserView, 
                    DestroyCustomUserView, 
                    UpdateCustomUserSingle, 
                    ListCreateCustomUserSingle, 
                    RetrieveUpdateCustomUserSingle, 
                    RetrieveDestroyCustomUserSingle, 
                    RetrieveUpdateDestroyCustomUserSingle, 
                    get_users_decorator, 
                    CustomUserViewSet,
                    CustomUserModelView,
                    test, 
                    testkwargs)

# define the router
router = routers.DefaultRouter()
  
# define the router path and viewset to be used
router.register('customusers', CustomUserViewSet, basename='customusers')
router.register('useractions', CustomUserModelView, basename='useractions')

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
    path('api/', include(router.urls)),
    path('test/<int:pk>/', test, name='test'),
    path('testkwargs/', testkwargs, name='testkwargs'),
]
