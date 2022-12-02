from django.shortcuts import render, get_object_or_404, redirect
from todos.models import TodoList, TodoItem
from todos.forms import TodoListForm

# Create your views here.
def todo_list_list(request):
    todos = TodoList.objects.all()
    context = {
        "todo_list_list": todos,
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
            list = form.save()
            list.save()
            return redirect("todo_list_detail", id=list.id)
    else:
        form = TodoListForm()
        context = {
            "form": form,
        }
    return render(request, "todos/create.html", context)

def todo_list_update(request, id):
    todo = get_object_or_404(TodoList, id=id)
    if request.method == "POST":
        form = TodoListForm(request.POST, instance=todo)
        if form.is_valid():
            list = form.save()
            list.save()
            return redirect("todo_list_detail", id=list.id)
    else:
        form = TodoListForm(instance=todo)

    context = {
        "todo_object": todo,
        "form": form,
    }
    return render(request, "todos/edit.html", context)

def todo_list_delete(request, id):
    todo = TodoList.objects.get(id=id)
    if request.method == "POST":
        todo.delete()
        return redirect("todo_list_list")
    return render(request, "todos/delete.html")
