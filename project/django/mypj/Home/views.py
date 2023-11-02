from django.shortcuts import render
from .models import Todo

def home(request):
    All = Todo.objects.all()
    return render(request, "Home.html" , {"Todos" : All})


def sey_hello(request):
    person = {"name": "admin"}
    return render(request, "index.html", context=person)
