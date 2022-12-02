from django.forms import ModelForm
from todos.models import TodoList, TodoItem

class TodoListForm(ModelForm):
    error_css_class = "error-field"
    required_css_class = "required field"
    class Meta:
        model = TodoList
        fields = [
            "name",
        ]

class TodoItemForm(ModelForm):
    class Meta:
        model = TodoItem
        fields = "__all__"
