from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(response):
    return HttpResponse("<h1>Welcome to Dixon page 1</h1>")

def V1(response):
    return HttpResponse("<h1>view 1</h1>")    
