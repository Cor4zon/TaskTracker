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
        # queryset = Project.objects.filter()
        projects = ProjectService.list()
        serializer = ProjectSerializer(projects, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        project = ProjectService.get(pk)
        serializer = ProjectSerializer(project)
        return Response(serializer.data)

    def create(self, request):
        title = request.POST.get("title")
        description = request.POST.get("description")
        deadline = request.POST.get("deadline")
        new_project = Project(title=title, description=description, tasksCount=0, deadline=deadline)

        ProjectService.add(new_project)
        # new_project.save()
        serializer = ProjectSerializer(new_project)
        return Response(serializer.data)

    def destroy(self, request, pk=None):
        ProjectService.delete(pk)
        return JsonResponse({'status': 'OK', 'message': 'You deleted project'}, status=200)


class TaskViewSet(viewsets.ViewSet):
    serializer_class = TaskSerializer

    def list(self, request, project_pk=None, pk=None):
        tasks = TaskService.get_filtered({"project": project_pk})
        serializer = TaskSerializer(tasks, many=True)
        return Response(serializer.data)

    def retrieve(self, request, project_pk=None, pk=None):
        task = TaskService.get(pk)
        serializer = TaskSerializer(task)
        return Response(serializer.data)

    def create(self, request, project_pk=None):
        title = request.data["title"]
        description = request.data["description"]
        status = request.data["status"]
        deadline = request.data["deadline"]
        new_task = Task(title=title, description=description, deadline=deadline, project_id=project_pk)

        TaskService.add(new_task)

        serializer = TaskSerializer(new_task)
        return Response(serializer.data)

    def destroy(self, request, project_pk=None, pk=None):
        TaskService.delete(pk)
        return JsonResponse({'status': 'OK', 'message': 'You deleted task'}, status=200)

