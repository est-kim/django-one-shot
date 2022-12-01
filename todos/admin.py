from django.contrib import admin
from todos.models import TodoList, TodoItem

# Register your models here.
@admin.register(TodoList)
class ToDoListAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "id",
    )

@admin.register(TodoItem)
class ToDoItemAdmin(admin.ModelAdmin):
    list_display = (
        "task",
        "due_date",
        "is_completed",
    )
