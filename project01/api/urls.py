from django.urls import path

from api.views import api_index, get_all_todos, HomePageView, add_todo, complete_todo, delete_completed, GetToDoView

app_name = 'todos'

urlpatterns = [
    path('', api_index, name='api_index'),
    path('todos/', get_all_todos, name='get_all_todos'),
    path('homepage', HomePageView.as_view(), name='homepage'),
    path("add", add_todo, name="add_todo"),
    path("completed/<todo_id>", complete_todo, name="complete_todo"),
    path("delete_completed", delete_completed, name="delete_completed"),
    path("getview", GetToDoView.as_view(), name="getview")
]
