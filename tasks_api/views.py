from django.shortcuts import get_object_or_404
from tasks.models import Project, Task, Comment
from .serializers import ProjectSerializer, TaskSerializer, CommentSerializer

from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework import viewsets


class ProjectViewSet(viewsets.ViewSet):
    serializer_class = ProjectSerializer

    def list(self, request):
        queryset = Project.objects.filter()
        serializer = ProjectSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = Project.objects.filter()
        project = get_object_or_404(queryset, pk=pk)
        serializer = ProjectSerializer(project)
        return Response(serializer.data)

    def create(self, request):
        title = request.POST.get("title")
        description = request.POST.get("description")
        deadline = request.POST.get("deadline")
        new_project = Project(title=title, description=description, tasksCount=0, deadline=deadline)
        new_project.save()
        serializer = ProjectSerializer(new_project)
        return Response(serializer.data)

    def destroy(self, request, pk=None):
        Project.objects.filter(pk=pk).delete()
        return JsonResponse({'status': 'OK', 'message': 'You deleted project'}, status=200)


class TaskViewSet(viewsets.ViewSet):
    serializer_class = TaskSerializer

    def list(self, request, project_pk=None):
        queryset = Task.objects.filter(project_id=project_pk)
        serializer = TaskSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None, project_pk=None):
        queryset = Task.objects.filter(pk=pk, project_id=project_pk)
        task = get_object_or_404(queryset, pk=pk)
        serializer = TaskSerializer(task)
        return Response(serializer.data)

    def create(self, request, project_pk=None):
        title = request.POST.get("title")
        description = request.POST.get("description")
        status = request.POST.get("status")
        deadline = request.POST.get("deadline")
        new_task = Task(title=title, description=description, deadline=deadline, project_id=project_pk)
        new_task.save()

        serializer = TaskSerializer(new_task)
        return Response(serializer.data)

    def destroy(self, request, pk=None, project_pk=None):
        Task.objects.filter(pk=pk).delete()
        return JsonResponse({'status': 'OK', 'message': 'You deleted task'}, status=200)

