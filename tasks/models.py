import datetime

from django.db import models
from users.models import Employee


class Project(models.Model):
    title = models.CharField(max_length=30)
    description = models.TextField()
    tasksCount = models.IntegerField(default=0)
    deadline = models.DateField(default=None)


class Task(models.Model):
    title = models.CharField(max_length=30)
    project = models.ForeignKey(Project, on_delete = models.CASCADE, default=None)
    description = models.TextField()
    status = models.IntegerField(blank=True, default=0)
    deadline = models.DateField(blank=True)
    # указывает на задачу предка
    subtask = models.IntegerField(blank=True, default=0)
    employee = models.ManyToManyField(Employee)


class Comment(models.Model):
    author = models.CharField(max_length=60)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    task = models.ForeignKey('Task', on_delete=models.CASCADE)
