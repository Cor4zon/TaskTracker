import datetime

from django.db import models
from users.models import Employee

# Create your models here.
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
    title = models.CharField(max_length=50)
    description = models.TextField()
    employee = models.ForeignKey(Employee, on_delete = models.CASCADE)
    task = models.ManyToManyField(Task)
