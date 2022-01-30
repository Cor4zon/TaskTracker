# users/urls.py

from django.urls import re_path, include, path
from users import views

app_name = "users"

urlpatterns = [
    re_path(r"^accounts/", include("django.contrib.auth.urls")),
    re_path(r"all_employees", views.all_employees, name="all_employees"),
    path("personal_data/<int:pk>", views.personal_data, name="personal_data"),
]