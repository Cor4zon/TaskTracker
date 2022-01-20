# tasks/serializers.py
from rest_framework import serializers
from tasks.models import Project, Task, Comment


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'


class TaskSerializer(serializers.ModelSerializer):
    parent_lookup_kwargs = {
        'project_pk': 'project__pk',
    }

    class Meta:
        model = Task
        fields = '__all__'


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'
