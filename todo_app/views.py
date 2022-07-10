from django.shortcuts import render
from .models import ToDoList, ToDoTask
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

# Create your views here.


# A view to represent all created list objects as a list
class ToDoListListView(ListView):

    model = ToDoList
    template_name = "todo_app/index.html"


# A view to represent all created task objects as a list
class ToDoTaskListView(ListView):

    model = ToDoTask
    template_name = "todo_app/todo_list.html"

    # Helps restrict the retrieval of tasks, by retrieving all tasks belonging to a chosen list
    def get_queryset(self):
        return ToDoTask.objects.filter(todo_list_id=self.kwargs["list_id"])

    # Returns a dictionary containing data available for render
    def get_context_data(self):
        # Inclusion of corresponding list object along with task object
        context = super().get_context_data()
        context["todo_list"] = ToDoList.objects.get(id=self.kwargs["list_id"])
        return context


# A view to create a new list
class CreateToDoList(CreateView):

    model = ToDoList
    fields = ["title"]

    def get_context_data(self):
        context = super().get_context_data()
        context["title"] = "Add a new list"
        return context


# A view to create a new task
class CreateToDoTask(CreateView):

    model = ToDoTask
    fields = ["title", "description", "due_timestamp", "todo_list"]

    # Return initial data for use on the form in this view
    def get_initial(self):
        initial_data = super().get_initial()
        todo_list = ToDoList.objects.get(id=self.kwargs["list_id"])
        initial_data["todo_list"] = todo_list
        return initial_data

    def get_context_data(self):
        context = super().get_context_data()
        todo_list = ToDoList.objects.get(id=self.kwargs["list_id"])
        context["todo_list"] = todo_list
        context["title"] = "Create a new task"
        return context

    # Provides URL to redirect to, after successfully creating a new task
    def get_success_url(self):
        return reverse("list", args=[self.object.todo_list_id])


# A view to update an existing task
class UpdateToDoTask(UpdateView):

    model = ToDoTask
    fields = ["title", "description", "due_timestamp", "todo_list"]

    def get_context_data(self):
        context = super().get_context_data()
        context["todo_list"] = self.object.todo_list
        context["title"] = "Edit item"
        return context

    def get_success_url(self):
        return reverse("list", args=[self.object.todo_list_id])


# A view to delete an existing list
class ToDoListDelete(DeleteView):

    model = ToDoList
    # Using reverse_lazy() instead of reverse() allows loading of URLs when file is imported
    success_url = reverse_lazy("index")


# A view to delete an existing task
class ToDoTaskDelete(DeleteView):

    model = ToDoTask

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["todo_list"] = self.object.todo_list
        return context

    def get_success_url(self):
        return reverse_lazy("list", args=[self.kwargs["list_id"]])