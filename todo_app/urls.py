from django.urls import path
from .views import ToDoListListView, ToDoTaskListView, CreateToDoList, CreateToDoTask, UpdateToDoTask, ToDoListDelete, \
    ToDoTaskDelete

urlpatterns = [
    path("", ToDoListListView.as_view(), name="index"),
    path("list/<int:list_id>/", ToDoTaskListView.as_view(), name="list"),
    path("list/add/", CreateToDoList.as_view(), name="list-add"),
    path("list/<int:list_id>/task/add/", CreateToDoTask.as_view(), name="task-add"),
    path("list/<int:list_id>/task/<int:pk>/", UpdateToDoTask.as_view(), name="task-update"),
    path("list/<int:pk>/delete/", ToDoListDelete.as_view(), name="list-delete"),
    path("list/<int:list_id>/task/<int:pk>/delete/", ToDoTaskDelete.as_view(), name="task-delete"),
]
