# tasks/serializers.py
from rest_framework import serializers
from .models import Task, Comment, Project

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ["id", "title", "description", "tasksCount", "deadline"]
