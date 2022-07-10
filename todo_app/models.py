from django.db import models
from django.urls import reverse
from django.utils import timezone

# Create your models here.


# Django ORM to a DB containing all created lists
class ToDoList(models.Model):

    title = models.CharField(max_length=25, null=False, unique=True)

    # To display a list by its title in the admin interface
    def __str__(self):
        return self.title

    # reverse() returns an absolute path reference (URL without the domain name) matching a given view/callable view
    # object
    def get_absolute_url(self):
        return reverse("list", args=[self.id])


# Django ORM to a DB containing all created tasks
class ToDoTask(models.Model):

    title = models.CharField(max_length=25, null=False, unique=True)
    description = models.TextField(blank=True)
    start_timestamp = models.DateTimeField(auto_now_add=True)
    due_timestamp = models.DateTimeField(default=timezone.now() + timezone.timedelta(hours=6))

    # A foreign key linking each task to a unique list
    todo_list = models.ForeignKey(ToDoList, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("task-update", args=[str(self.todo_list.id), str(self.id)])
