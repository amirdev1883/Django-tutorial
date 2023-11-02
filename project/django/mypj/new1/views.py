from django.shortcuts import render
from django.http import HttpResponse


def mew(request):
    return render(request , "mew.html")
