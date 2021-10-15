# tasks/urls.py
from django.urls import path, re_path, include
from django.conf.urls import url
from tasks import views

urlpatterns = [
    url(r"^$", views.index, name="tasks")
]