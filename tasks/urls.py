# tasks/urls.py
from django.urls import path, re_path, include
from django.conf.urls import url
from tasks import views

app_name = "tasks"

urlpatterns = [
    url(r"^$", views.index, name="tasks"),
    url(r"all_projects", views.all_projects, name="all_projects"),
    path('project_info/<int:pk>', views.project_info, name="project_info"),
    path('project_tasks/<int:pk>', views.project_tasks, name="project_tasks"),
    path('task_info/<int:pk>', views.task_info, name="task_info"),
]