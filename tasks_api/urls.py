# tasks_api/urls.py

from django.urls import path, include
from rest_framework.routers import DefaultRouter

from rest_framework_nested import routers


from .views import ProjectViewSet, TaskViewSet

# router = DefaultRouter()
# router.register(r"projects", ProjectViewSet)
#
# urlpatterns = [
#     path("", include(router.urls))
# ]

router = routers.SimpleRouter()
router.register(r"projects", ProjectViewSet)

project_router = routers.NestedSimpleRouter(router, r'projects', lookup='project')
project_router.register(r'tasks', TaskViewSet)


urlpatterns = [
    path(r'', include(router.urls)),
    path(r'', include(project_router.urls)),
]