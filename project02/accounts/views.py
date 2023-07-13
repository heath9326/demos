from django.shortcuts import render
from django.http import HttpResponse

# Project specific:
from .models import CustomUser
from .serializers import CustomUserSerializer

# REST
from rest_framework.response import Response
from rest_framework.decorators import api_view, schema
from rest_framework.views import APIView
from rest_framework import status
from rest_framework import generics as drf_generics



# Through class view
class GetCustomUsersView(APIView):
    serializer_class = CustomUserSerializer

    def get(self, request):
        queryset = CustomUser.objects.all().order_by('id')
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
        
    def delete(self, request, pk):
        user = CustomUser.objects.filter(id=pk)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
        
# Through function-based view using a decorator
@api_view(['GET', 'POST'])
def get_users(request):
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
    else:
        return Response({'error': 'Type of request is not handled yet!'}, status=400)
    

# This view functions as an alternative to APIView get
class CustomUserListAPIView(drf_generics.ListAPIView):
    serializer_class = CustomUserSerializer
    queryset = CustomUser.objects.all()

class SingleUserRetrieveView(drf_generics.RetrieveAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer





# Test Views
def test(request, pk):
    id = pk
    return HttpResponse('ID is %s' % id)

# def testkwargs(request):
#     id = request.query_params('id')
#     return HttpResponse('ID is %s' % id)