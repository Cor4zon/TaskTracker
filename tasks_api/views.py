from django.shortcuts import get_object_or_404
from tasks.models import Project, Task, Comment
from .serializers import ProjectSerializer, TaskSerializer, CommentSerializer

from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework import viewsets

from .repository_pattern import ProjectService, TaskService


class ProjectViewSet(viewsets.ViewSet):
    serializer_class = ProjectSerializer

    def list(self, request):
        projects = ProjectService.read_all()
        serializer = ProjectSerializer(projects, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        project = ProjectService.read(pk)
        serializer = ProjectSerializer(project, many=True)
        return Response(serializer.data)

    def create(self, request):
        new_project = request.data
        ProjectService.create(new_project)
        serializer = ProjectSerializer(new_project)
        return Response(serializer.data)

    def destroy(self, request, pk=None):
        ProjectService.delete(pk)
        return JsonResponse({'status': 'OK', 'message': 'You deleted project'}, status=200)

    def partial_update(self, request, pk):
        ProjectService.update(pk, request.data)
        return JsonResponse({'status': 'OK', 'message': 'You update project'}, status=200)


class TaskViewSet(viewsets.ViewSet):
    serializer_class = TaskSerializer

    def list(self, request, project_pk=None, pk=None):
        tasks = TaskService.read_filtered({"project": project_pk})
        serializer = TaskSerializer(tasks, many=True)
        return Response(serializer.data)

    def retrieve(self, request, project_pk=None, pk=None):
        task = TaskService.read(pk)
        serializer = TaskSerializer(task)
        return Response(serializer.data)

    def create(self, request, project_pk=None):
        new_task = request.data
        TaskService.create(new_task)
        return Response(new_task)

    def destroy(self, request, project_pk=None, pk=None):
        TaskService.delete(pk)
        return JsonResponse({'status': 'OK', 'message': 'You deleted task'}, status=200)

