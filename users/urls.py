# users/urls.py

from django.urls import path, re_path, include
from django.conf.urls import url
from users import views

app_name = "users"

urlpatterns = [
    url(r"^accounts/", include("django.contrib.auth.urls")),
    url(r"all_employees", views.all_employees, name="all_employees"),
    path("personal_data/<int:pk>", views.personal_data, name="personal_data"),
]