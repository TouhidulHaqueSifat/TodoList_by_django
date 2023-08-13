from django.contrib import admin
from first_app.models import TodoList

# Register your models here.

class TodoListAdmin(admin.ModelAdmin):
    list_display = ['task_title', 'task_description', 'completed']

admin.site.register(TodoList, TodoListAdmin)