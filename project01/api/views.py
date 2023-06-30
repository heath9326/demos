from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from django.views import generic
from django.views.decorators.http import require_POST

#For DRF
from rest_framework.response import Response
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

class GetToDoView(APIView):
    def get(self, request):
        user = request.user
        #Get the contance of ToDos tables:
        queryset = ToDo.objects.all().filter(user=user).order_by("id").values()
        # Serializing extracted information
        serilizer_for_queryset = ToDoSerializer(instance=queryset, many=True)
        # Give serialized data to the view
        return Response(serilizer_for_queryset.data)


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

