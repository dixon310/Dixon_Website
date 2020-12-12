from django.shortcuts import render
from django.http import HttpResponse
from .models import ToDoList, Item
# Create your views here.

def index(response, name):
    ls = ToDoList.objects.get(name=name)
    item = ls.item_set.get(id=1)
    return render(response, "main/base.html", {})

def home(response):
    return render(response, "main/home.html", {})
