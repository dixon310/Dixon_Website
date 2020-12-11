from django.urls import path
from . import views

urlpatterns = [
    path("<str:name>", views.index, name="index"),
    path("v1/", views.index, name="view 1"),
    ]
