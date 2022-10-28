from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("addTask/", views.addTask, name="addTask"),
    path("editTask/<str:id>", views.editTask, name="editTask"),
    path("completeTask/<str:id>", views.completeTask, name="completeTask")
]
