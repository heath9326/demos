from django.shortcuts import render
from django.http import HttpResponse

# Project specific:
from .models import CustomUser
from .serializers import CustomUserSerializer, CustomUserHyperlinkedSerializer
from common.renderes import PlainTextRenderer

# REST
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework import status
from rest_framework import generics as drf_generics
from rest_framework.permissions import IsAdminUser
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework import renderers
from rest_framework.throttling import UserRateThrottle
from django.core.exceptions import ObjectDoesNotExist

# Tools
from datetime import datetime
from django.shortcuts import get_object_or_404


# Through class view
class GetCustomUsersView(APIView):
    serializer_class = CustomUserSerializer


    def get_queryset(self):
        users = CustomUser.objects.all()
        return users

    #Test get request for TemplateHTMLRenderer
    # def get(self, request, *args, **kwargs):

    #     try:
    #         id = request.query_params['id']
    #         if id != None:
    #             data = CustomUser.objects.get(id=id)
    #     except:
    #         data = self.get_queryset()

    #     #Template for rendering needs to be customized for it to work    
    #     return Response({'data': data}, template_name='users.html')    

    def get(self, request, *args, **kwargs):
        print(request.GET)
        id = request.GET['id']

        user = get_object_or_404(CustomUser, pk=id)

        
        try:
            id = request.query_params['id']

            if id != None:
                user = CustomUser.objects.get(id=id)
                serializer = CustomUserSerializer(user)
        except ObjectDoesNotExist:
            return Response("CustomUser with this id does not exist.")
        except:
            queryset = self.get_queryset()
            serializer = CustomUserSerializer(instance=queryset, many=True)

        return Response(serializer.data)
    

    def post(self, request):
        serializer = CustomUserSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
            # How do I reaload the page
        else:
            return Response(serializer.errors, status=400)


    # Another way of implementing post:    
    # def post(self, request, *args, **kwargs):
    #     user_data = request.data

    #     new_user = CustomUser.objects.create(username=user_data["username"], email=user_data[
    #         "email"], password=cuser_data["password"])
    #     new_user.save()
    #     serializer = CarsSerializer(new_user)

    #     return Response(serializer.data)


    # Needs testing
    def put(self, request, *args, **kwargs):
        # Works (needs data in JSON format and id in kwargs)
        id = request.query_params["id"]
        user_object = CustomUser.objects.get(id=id)

        data = request.data

        user_object.password = data["password"]
        user_object.last_login = data["last_login"]
        user_object.is_superuser = data["is_superuser"]
        user_object.username = data["username"]
        user_object.first_name= data["first_name"]
        user_object.last_name= data["last_name"]
        user_object.is_staff= data["is_staff"]
        user_object.is_active= data["is_active"]
        user_object.data_joined = data["date_joined"]
        user_object.email = data["email"]

        user_object.save()

        serializer = CustomUserSerializer(user_object)
        return Response(serializer.data)
    

    def patch(self, request, *args, **kwargs):
        # Works (needs data in JSON format and id in kwargs) 
        id = request.query_params["id"]
        user_object = CustomUser.objects.get(id=id)
        data = request.data

        user_object.username = data.get("username", user_object.username)
        user_object.email = data.get("email", user_object.email)
        user_object.password = data.get("password", user_object.password)

        user_object.save()
        serializer = CustomUserSerializer(user_object)

        return Response(serializer.data)
        

class DeleteCustomUserView(APIView):
    def delete(self, request, pk):
        user = CustomUser.objects.filter(id=pk)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    

# Through function-based view using a decorator
@api_view(['GET', 'POST', 'PUT', 'PATCH', 'DELETE'])
def get_users_decorator(request):
    # Does not render and HTTP 
    renderer_classes = [CustomUserSerializer]
    
    if request.method == 'GET':
        queryset = CustomUser.objects.all().order_by('id')
        serializer = CustomUserSerializer(instance=queryset, many=True)

        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = CustomUserSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=400)

    elif request.method == "PUT":
        id = request.query_params["id"]
        user_object = CustomUser.objects.get(id=id)
        serializer = CustomUserSerializer(user_object, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == "PATCH":
        id = request.query_params["id"]
        user_object = CustomUser.objects.get(id=id)
        serializer = CustomUserSerializer(user_object, data=request.data, partial=True) 

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == "DELETE":
        id = request.query_params["id"]
        user = CustomUser.objects.filter(id=id)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    else:
        return Response({'error': 'Type of request is not handled yet!'}, status=400)


class CustomUserViewSet(viewsets.ViewSet):
    ''' 
    ModelViewSet that handles the same functions as main APIView

    '''
    serializer = CustomUserSerializer
    queryset = CustomUser.objects.all()
    
    def list(self, request):
        serializer = self.serializer(instance=self.queryset, many=True)    
        return Response(serializer.data)
    
    def create(self, request, pk=None):
        data = request.data
        serializer = self.serializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=400)

    def destroy(self, request, pk=None):
        user = get_object_or_404(self.queryset, pk=pk)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    def retrieve(self, request, pk=None):
        user = get_object_or_404(self.queryset, pk=pk)
        serializer = self.serializer(user)
        return Response(serializer.data)

    def update(self, request, pk=None):
        user = get_object_or_404(self.queryset, pk=pk)

        data = request.data

        user.password = data["password"]
        user.last_login = data["last_login"]
        user.is_superuser = data["is_superuser"]
        user.username = data["username"]
        user.first_name= data["first_name"]
        user.last_name= data["last_name"]
        user.is_staff= data["is_staff"]
        user.is_active= data["is_active"]
        user.data_joined = data["date_joined"]
        user.email = data["email"]

        user.save()

        serializer = self.serializer(user)
        return Response(serializer.data)
    

    def partial_update(self, request, pk=None):
        user = get_object_or_404(self.queryset, pk=pk)
        data = request.data

        user.username = data.get("username", user.username)
        user.email = data.get("email", user.email)
        user.password = data.get("password", user.password)

        user.save()
        serializer = self.serializer(user)

        return Response(serializer.data)


class CustomUserModelView(viewsets.ModelViewSet):
    ''' 
    ViewSet that handles the same functions as main APIView

    '''
    serializer_class = CustomUserSerializer
    queryset = CustomUser.objects.all()

    # def list(self, request):
        #WORKS BY DEFAULT

    # def retrieve(self, request, pk=None):
        #WORKS BY DEFAULT

    #def create(self, request, pk=None):
        #WORKS BY DEFAULT
   
    #def update(self, request, pk=None)
        #WORKS BY DEFAULT

    #def partial_update(self, request, pk=None)
        #WORKS BY DEFAULT
    
    #def destroy(self, request, pk=None):
        #WORKS BY DEFAULT

    @action(detail=True, methods=['put', 'patch'], url_path='inactive')
    def inactive(self, request, *args, **kwargs):
        user = self.get_object()
        user.make_inactive()
        return Response({'status': 'inactive'})


# This view functions as an alternative to APIView get
class CustomUserListAPIView(drf_generics.ListAPIView):
    serializer_class = CustomUserSerializer
    queryset = CustomUser.objects.all()


class SingleUserRetrieveView(drf_generics.RetrieveAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer


class DestroyCustomUserView(drf_generics.DestroyAPIView):
    permission_classes = (IsAdminUser, )

    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer


class UpdateCustomUserSingle(drf_generics.UpdateAPIView):
    #FIXME works, but does not hash passwords
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer


class ListCreateCustomUserSingle(drf_generics.ListCreateAPIView):
    serializer_class = CustomUserSerializer

    def get_queryset(self):
        return CustomUser.objects.filter(date_joined__contains=datetime.today().date())


class RetrieveUpdateCustomUserSingle(drf_generics.RetrieveUpdateAPIView):
    serializer_class = CustomUserSerializer
    lookup_field = 'username'

    def get_object(self):
        username = self.kwargs['username']
        return get_object_or_404(CustomUser, username=username)


class RetrieveDestroyCustomUserSingle(drf_generics.RetrieveDestroyAPIView):
    serializer_class = CustomUserSerializer
    lookup_field = 'email'

    def get_object(self):
        email = self.kwargs['email']
        return get_object_or_404(CustomUser, email=email)


class RetrieveUpdateDestroyCustomUserSingle(drf_generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CustomUserSerializer
    lookup_field = 'email'

    def get_object(self):
        email = self.kwargs['email']
        return get_object_or_404(CustomUser, email=email)

#FIXME: Не работает от слова совсем
class CustomUserHyperlinkedAPI(APIView):
    serializer_class = CustomUserHyperlinkedSerializer
    
    def get_queryset(self):
        users = CustomUser.objects.all()
        return users
    
    def get(self, request):
        queryset = self.get_queryset()
        serializer_context = {
            'request': request,
        }
        serializer = CustomUserHyperlinkedSerializer(instance=queryset, context=serializer_context, many=True)
        return Response(serializer.data)




# Test Views
def test(request, pk):
    id = pk
    return HttpResponse('ID is %s' % id)

def testkwargs(request):
    id = request.GET.get('id')
    return HttpResponse('ID is %s' % id)