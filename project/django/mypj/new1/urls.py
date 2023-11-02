from django.urls import path
from . import views

urlpatterns = [
    path("mew/", views.mew),
]
