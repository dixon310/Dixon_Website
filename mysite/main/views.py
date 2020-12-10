from django.shortcuts import render
from django.http import HttpResponse
from .models import ToDoList, Item
# Create your views here.

def index(response, id):
    return HttpResponse("<h1>Welcome to Dixon page 1</h1>" % id)

def V1(response):
    return HttpResponse("<h1>view 1</h1>")
