from django.contrib import admin
from todos.models import TodoList

# Register your models here.
@admin.register(TodoList)
class ToDoListAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "id",
    )
