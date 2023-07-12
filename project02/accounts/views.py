from django.shortcuts import render

# Project specific:
from .models import CustomUser
from .serializers import CustomUserSerializer

# REST
from rest_framework.response import Response
from rest_framework.views import APIView


# Create your views here.
class GetCustomUsersView(APIView):
    def get(self, request):
        queryset = CustomUser.objects.all().order_by('id')
        serializer = CustomUserSerializer(instanse=queryset, many=True)

        return Response(serializer.data)
