# from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name = "blogHome"),
    # path("blogpost/", views.blogpost, name = "blogPost")
    path("blogpost/<int:pid>", views.blogpost, name = "blogPost")
]
