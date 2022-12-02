from django.forms import ModelForm
from todos.models import TodoList

class TodoListForm(ModelForm):
    error_css_class = "error-field"
    required_css_class = "required field"
    class Meta:
        model = TodoList
        fields = [
            "name",
        ]
