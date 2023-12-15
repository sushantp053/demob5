from django.contrib import admin
from django.urls import include, path
from home import views

urlpatterns = [
    path("", views.index),
    path("home", views.home),
    path("about", views.about),
    path("student", views.student),
    path("addstudent", views.addStudent),
    path("addstud", views.addStud),
    path("login", views.loginUser),
    path("loginUser", views.loginUser),
    path("logout", views.logoutUser),
    path("demoapi", views.demoapi),
    path("details/<int:id>", views.details),
    path("edit/<int:id>", views.edit),
    path("update", views.update),
    path("delete/<int:id>", views.delete), 
]