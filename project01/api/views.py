from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from django.views import generic
from django.views.decorators.http import require_POST

# Import app specific elements
from api.models import ToDo
from api.forms import CreateToDo


# Create your views here.
class HomePageView(generic.TemplateView):
    template_name = "home.html"
    add_form = CreateToDo
    def get(self, request):
        if request.method == "GET":
            todos = ToDo.objects.all().order_by("id").values()
            args = {"todos": todos, "add_todo": self.add_form}
            return render(request, self.template_name, args)

# Form action views that redirect to home
@require_POST
def add_todo(request):
    # Initialize the form:
    form = CreateToDo(request.POST)

    if form.is_valid():
        # Create the instance of the class:
        new_todo = ToDo(body=request.POST["body"])
        new_todo.save()
        return redirect("homepage")


def complete_todo(request, todo_id):
    # Get object id on click:
    thing = ToDo.objects.get(pk=todo_id)
    # Set its status to completed
    thing.completed = True
    # Save
    thing.save()
    return redirect("homepage")

def delete_completed(request):
    ToDo.objects.filter(completed=True).delete()
    return redirect("homepage")


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

