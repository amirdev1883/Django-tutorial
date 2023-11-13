from django.shortcuts import render, redirect
from .models import Todo
from django.contrib import messages
from .forms import TodoCreateForms, TodoUpdateForm


def home(request):
    All = Todo.objects.all()
    return render(request, "Home.html", {"Todos": All})


def detail(request, todo_id):
    todo = Todo.objects.get(id=todo_id)
    return render(request, 'detail.html', {"todo": todo})


def delete(request, todo_id):
    Todo.objects.get(id=todo_id).delete()
    messages.success(request, 'you deleted successfully')
    return redirect('home')


def create(request):
    if request.method == 'POST':
        form = TodoCreateForms(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            Todo.objects.create(title=cd['title'], body=cd['body'], created=cd['created'])
            messages.success(request, "Todo created successfully ", 'success')
            return redirect('home')

    else:
        form = TodoCreateForms
    return render(request, 'CreateForm.html', {"form": form})


def update(request, todo_id):
    todo = Todo.objects.get(id=todo_id)
    if request.method == "POST":
        form = TodoUpdateForm(request.POST, instance=todo)
        if form.is_valid():
            form.save()
            messages.success(request, "your todo updated successfully ", "success")
            return redirect("detail", todo_id)
    else:
        form = TodoUpdateForm(instance=todo)
        return render(request, 'Update.html', {'form': form})
