from django.contrib import admin
from .models import ToDoList, ToDoTask

# Registration of models with the admin interface (facilitates CRUD operations)

admin.site.register(ToDoList)
admin.site.register(ToDoTask)
