from django.shortcuts import render, get_object_or_404, redirect
from todos.models import TodoList, TodoItem
from todos.forms import TodoListForm

# Create your views here.
def todo_list(request):
    todos = TodoList.objects.all()
    context = {
        "todo_list": todos,
    }
    return render(request, "todos/list.html", context)

def todo_list_detail(request, id):
    todos = get_object_or_404(TodoList, id=id)
    tasks = TodoItem.objects.all()
    context = {
        "todo_list_object": todos,
        "tasks": tasks,
    }
    return render(request, "todos/detail.html", context)

def todo_list_create(request):
    if request.method == "POST":
        form = TodoListForm(request.POST)
        if form.is_valid():
            todo = form.save(False)
            todo.save()
            return redirect("todo_list_list")
    else:
        form = TodoListForm()
        context = {
            "form": form,
        }
    return render(request, "todos/create.html", context)
