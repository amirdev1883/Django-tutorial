# Django

## Session 1 : create project

create a virtual environment for your project

`python -m vnev myvenv`

now your venv(virtual environment ) is created 

then you have to activate it

`myvenv/Scripts/activate.bat`

`(myvenv) C:\Users\AmirAbbas\Desktop\test>`

it should be like this

### install the Django by this command

`pip install Django`

`Django-admin startproject mypj`

![](Screenshot%202023-11-01%20120115.jpg "optional-title")

then you have a manage.py that is a tool to work with your project and your project folder .

### use a texteditor (I prefer pycharm) 


Go to setting and change the interpreter and chose your venv for terminal

### folow this setps:
1 .Go to pycharm's setting
![](images/2.jpg "optional-title")

2.Select project then python interpreter

![](images/3.jpg "optional-title")

3.Select the interpreter address 

yourenv > Scripts > python.exe

![](images/4.jpg "optional-title")

4.Press ok button then apply this change 

![](images/5.jpg "optional-title")

## Lets run our project for first time 

`python manage.py runserver`

you have something like error that is about migration

`python manage.py migrate`

Django will create a database by default sqllight

you can check the database information in setting.py 

## MVT

```mermaid
graph TD
Model --> View;
Template --> View;

View --> URL
URL --> View

Django --> URL
URL --> Django

Django --> User
User --> Django
```
## creating a user for access Django admin panel

`python manage.py createsuperuser`

then enter username and password for user 

## creatin App 

`python manage.py startapp myapp`

create urls.py file in your new app 

then you have to know Django about your new app

go to setting.py and add the new app name in INSTALLED_APPS list

![](images/6.jpg "optional-title")

```python
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "Home",
    'new1',
]
```
like this

create a url for your app
### urls.py
```python
from django.urls import path
from . import views

urlpatterns = [
    path("new/", views.mew),
]
```
### views.py
```python
from django.shortcuts import render
def mew(request):
    pass
```

all views functions have to give request 

lets make view.py better 
```python
from django.shortcuts import render
from django.http import HttpResponse

def mew():
    return HttpResponse("mew user")

```
## Add app's Url to project
### mypj > urls.py 
check that include imported 
```python
from django.contrib import admin
from django.urls import path, include
```
```python 
urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("Home.urls")),
    #add this path and use include
    path("new/", include("new1.urls"))

]
```
## Templates

#### Create a folder and name it Templates
then you have to add it to your project 

go to setting.py 
```python
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]
```
and add the templates in DIRS
```python
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "Templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]
```

create html file to show to clients 

```python
def mew(request):
    return render(request , "mew.html")
```
## variable in template 

you can show variable in html file in {{ variable }}
like this .

you can send information from views to template with
context 
```python
def cat(request):
    Catinfo = {"name": "my-cat", "sound": "mew-mew"}
    return render(request, "cat.html", context=Catinfo)
```
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>cat</title>
</head>
<body>
    <h1>{{name}}</h1>
    <h1>{{sound}}</h1>
</body>
</html>
```

## Operators in template

you can write python operator code like if else for and ...
with {% %} that's called tags in Django

```html
    {%if name == 'my-cat' %}
        <h1> hello little cat pus pus</h1>
    {%endif%}
```
## Filter in template
```html
    <h1>{{name|upper}}</h1>
    <h1>{{sound|title}}</h1>
```
## comment in template

    {# This is a comment #}
it should not be appear in website page

## Models

after create a app Django automatically generate a models.py
in app directory 

models is for Databases and it save some information about users 
and ...

create a class with camelcase name and enter fields that you need
for database

class should inherit models.model 

``` python
from django.db import models

class Todo(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField()
    deadline = models.DateTimeField()
```
[Field types Django](https://docs.djangoproject.com/en/4.2/ref/models/fields/#field-types)
< -- all field types in Django documentation

you have to convert this to sqllight whit this command

`python manage.py makemigrations`

this fields will come to migrations folder 
and if you want to change something its ok
change it and then enter this command again 


`python manage.py migrate`for convert field to database


## Add models to admin panel

go to admin.py and write this code
```python
from .models import Todocat
admin.site.register(Todocat)
```
go to admin panel and you have Todocat informations

![](images/7.jpg "optional-title")

you have your app name then Todocat

