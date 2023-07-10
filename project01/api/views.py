from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from django.views import generic
from rest_framework import generics as drf_generics
from django.views.decorators.http import require_POST
from django.shortcuts import get_object_or_404

#For DRF
from rest_framework.response import Response
# class GetToDoView(APIView):
from rest_framework.views import APIView
from rest_framework.decorators import api_view, permission_classes
from rest_framework import permissions

# Import app specific elements
from api.models import ToDo
from api.forms import CreateToDo
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from api.serializers import ToDoSerializer


# Create your views here.
class HomePageView(generic.TemplateView):
    template_name = "home.html"
    add_form = CreateToDo
    def get(self, request):
        if request.method == "GET":
            #First get which user is logger in:
            user = request.user
            #selects todos where user is user
            todos = ToDo.objects.all().filter(user=user).order_by("id").values()
            args = {"todos": todos, "add_todo": self.add_form}
            return render(request, self.template_name, args)


# Form action views that redirect to home
@login_required(login_url='login_page')
@require_POST
def add_todo(request):
    # Initialize the form:
    form = CreateToDo(request.POST)

    if form.is_valid():
        user = request.user
        # Create the instance of the class:
        new_todo = ToDo(body=request.POST["body"], user=user)
        new_todo.save()
        return redirect("todos:homepage")


@login_required(login_url='login_page')
def complete_todo(request, todo_id):
    # Get object id on click:
    thing = ToDo.objects.get(pk=todo_id)
    # Set its status to completed
    thing.completed = True
    # Save
    thing.save()
    return redirect("todos:homepage")


@login_required(login_url='login_page')
def delete_completed(request):
    user = request.user
    ToDo.objects.filter(completed=True, user=user).delete()
    return redirect("todos:homepage")


class GetToDoView(drf_generics.ListCreateAPIView):
    serializer_class = ToDoSerializer
    queryset = ToDo.objects.all()

# class GetToDoView(APIView):
#     def get(self, request):
#         user = request.user.username
#         #Get the contance of ToDos tables:
#         queryset = ToDo.objects.all().filter(user=user).order_by("id").values()
#         # Serializing extracted information
#         serilizer_for_queryset = ToDoSerializer(instance=queryset, many=True)
#         # Give serialized data to the view
#         return Response(serilizer_for_queryset.data)

# class GetToDoView(APIView):
#     def get(self, request):
#         user = request.user
#         queryset = ToDo.objects.all().filter(user=user).order_by("id").values()
#         serializer = ToDoSerializer(data=queryset)
#         if serializer.is_valid():
#             # Retrieve the validated data:
#             validated_data = serializer.validated_data

#             # Retrieve the object
#             username_slug = validated_data['user']
#             try:
#                 # Assigning value of the slug object to the field fixing the issue
#                 username = ToDo.objects.get(user=username_slug)
#             except ToDo.DoesNotExist:
#                 return Response({'error': 'Related object not found'}, status=400)
            
#             validated_data['user'] = username
#             serializer.save()
#             return Response(serializer.data, status=201)
        
#         return Response(serializer.errors, status=400)


    # def post(self, request):
    #     serializer = ToDoSerializer(data=request.data)

    #     if serializer.is_valid():
    #         # Retrieve the validated data:
    #         validated_data = serializer.validated_data

    #         # Retrieve the object
    #         username_slug = validated_data['user']
    #         try:
    #             # Assigning value of the slug object to the field fixing the issue
    #             username = ToDo.objects.get(user=username_slug)
    #         except ToDo.DoesNotExist:
    #             return Response({'error': 'Related object not found'}, status=400)
            
    #         validated_data['user'] = username
    #         serializer.save()

    #         return Response(serializer.data, status=201)
        
    #     return Response(serializer.errors, status=400)


def api_index(request):
    return HttpResponse('api index')


def get_all_todos(request):
    if request.method == "GET":
        todos = ToDo.objects.all()
        todos_json = []
        for i in todos:
            todos_json.append(i.json)
        return JsonResponse(dict(data=[i for i in todos_json]))
    return HttpResponse('HTTP method error')

