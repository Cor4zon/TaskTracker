# tasks/urls.py
from django.urls import re_path, include, path
from tasks import views


app_name = "tasks"

urlpatterns = [
    re_path(r"^$", views.index, name="tasks"),
    re_path(r"all_projects", views.all_projects, name="all_projects"),
    path('project_info/<int:pk>', views.project_info, name="project_info"),
    path('project_tasks/<int:pk>', views.project_tasks, name="project_tasks"),
    path('task_info/<int:pk>', views.task_info, name="task_info"),
    path('create_project', views.create_project, name="create_project"),
    path('project_info/<int:pk>/delete_project', views.delete_project, name="delete_project"),
    path('project_info/<int:pk>/delete_task', views.delete_task, name="delete_task"),
    path('task_info/delete_comment/<int:pk>', views.delete_comment, name="delete_comment"),
]
