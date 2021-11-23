from django.shortcuts import render, HttpResponse
from tasks.models import Project, Task, Comment
from tasks.forms import ProjectForm, TaskForm, CommentForm
from django.contrib.auth.decorators import login_required, user_passes_test


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
    tasks = Task.objects.filter(project_id=pk)
    return render(request, "project_tasks.html", context={"tasks": tasks})


@login_required
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

            comment.save()

    comments = Comment.objects.filter(task=task)

    return render(request, "task_info.html", context={"task": task, "form": form, "comments": comments})


@user_passes_test(lambda user: user.is_staff)
def create_project(request):
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


@user_passes_test(lambda user: user.is_staff)
def delete_project(request, pk):
    Project.objects.filter(pk=pk).delete()
    projects = Project.objects.all()
    return render(request, "all_projects.html", context={"projects": projects})


@user_passes_test(lambda user: user.is_staff)
def delete_task(request, pk):
    Task.objects.filter(pk=pk).delete()
    tasks = Task.objects.filter(project_id=pk)
    return render(request, "project_tasks.html", context={"tasks": tasks})

