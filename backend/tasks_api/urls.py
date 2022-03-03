# tasks_api/urls.py

from django.urls import path, include
from rest_framework.routers import DefaultRouter

from rest_framework_nested import routers
from .views import ProjectViewSet, TaskViewSet


router = routers.DefaultRouter()
router.register(r"projects", ProjectViewSet, basename='projects')
## generates:
# /projects/
# /pojects/{project_pk}/


project_router = routers.NestedSimpleRouter(router, r'projects', lookup='project')
project_router.register(r'tasks', TaskViewSet, basename='tasks')
## generates:
# /projects/{project_pk}/tasks/
# /projects/{project_pk}/tasks/{task_pk}/



urlpatterns = [
    path(r'', include(router.urls)),
    path(r'', include(project_router.urls)),
]