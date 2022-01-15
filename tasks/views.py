from django.shortcuts import render, HttpResponse
from tasks.models import Project, Task, Comment
from tasks.forms import ProjectForm, TaskForm, CommentForm
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required, user_passes_test
import redis

from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Project
from .serializers import ProjectSerializer

r = redis.Redis()


# Create your views here.
def index(request):
    return render(request, "tasks.html")


@login_required
def all_projects(request):
    projects = Project.objects.all()
    return render(request, "all_projects.html", context={"projects": projects})


@login_required
def project_info(request, pk):
    project = Project.objects.get(pk=pk)
    return render(request, "project_info.html", context={"project": project})


@login_required
def project_tasks(request, pk):
    # print(f"userid: {request.user.id}")
    # if str(request.user.groups.all()[0]) == 'boss':
    #     tasks = Task.objects.using('boss').filter(project_id=pk)
    #     return render(request, "project_tasks.html", context={"tasks": tasks})
    # elif str(request.user.groups.all()[0]) == 'staff':
    #     tasks = Task.objects.using('staff').filter(project_id=pk)
    #     return render(request, "project_tasks.html", context={"tasks": tasks})
    # else:
    #     return redirect("/tasks")
    tasks = Task.objects.filter(project_id=pk)
    return render(request, "project_tasks.html", context={"tasks": tasks})


def task_info(request, pk):
    task = Task.objects.get(pk=pk)
    form = CommentForm()
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = Comment(
                author=form.cleaned_data["author"],
                body=form.cleaned_data["body"],
                task=task
            )

            # increase_comment_count(pk)

            comment.save()

    comments = Comment.objects.filter(task=task)

    return render(request, "task_info.html", context={"task": task, "form": form, "comments": comments})


def create_project(request):
    # if not (str(request.user.groups.all()[0]) == 'boss'):
    #     return redirect("/tasks")

    if request.method == "POST":
        title = request.POST.get("title")
        description = request.POST.get("description")
        deadline = request.POST.get("deadline")
        new_project = Project(title=title, description=description, tasksCount=0, deadline=deadline)
        new_project.save()
        projects = Project.objects.all()
        return render(request, "all_projects.html", context={"projects": projects})
    else:
        projectform = ProjectForm()
        return render(request, "create_project.html", context={"form": projectform})


def delete_project(request, pk):
    # if str(request.user.groups.all()[0]) == 'boss':
    Project.objects.filter(pk=pk).delete()
    projects = Project.objects.all()
    return render(request, "all_projects.html", context={"projects": projects})
    # return redirect("/tasks")


# @user_passes_test(lambda user: user.is_staff)
def delete_task(request, pk):
    Task.objects.filter(pk=pk).delete()
    tasks = Task.objects.filter(project_id=pk)
    return render(request, "project_tasks.html", context={"tasks": tasks})


def delete_comment(request, pk):
    task_id = Comment.objects.filter(pk=pk)[0].task_id
    print(f"taskID:{task_id}")
    Comment.objects.filter(pk=pk).delete()
    # decrease_comment_count(task_id)

    return redirect(f"/tasks/task_info/{task_id}")


# def increase_comment_count(task_id):
#     print(r.hget(f"task:{task_id}", "counter"))
    # r.hincrby(f"task:{task_id}", "counter", 1)


# def decrease_comment_count(task_id):
#     print(r.hget(f"task:{task_id}", "counter"))
    # r.hincrby(f"task:{task_id}","counter", -1)
