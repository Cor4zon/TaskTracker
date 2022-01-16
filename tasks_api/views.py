from django.shortcuts import render
from tasks.models import Project, Task, Comment
from .serializers import ProjectSerializer, TaskSerializer, CommentSerializer

from rest_framework import viewsets


class ProjectViewSet(viewsets.ModelViewSet):
    serializer_class = ProjectSerializer
    queryset = Project.objects.all()


class TaskViewSet(viewsets.ModelViewSet):
    serializer_class = TaskSerializer
    queryset = Task.objects.all()


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()
