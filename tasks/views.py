from django.shortcuts import render

from tasks.models import Project, Task, Comment

# Create your views here.
def index(request):
    return render(request, "tasks.html")


def all_projects(request):
    projects = Project.objects.all()
    return render(request, "all_projects.html", context={"projects": projects})


def project_info(request, pk):
    project = Project.objects.get(pk=pk)
    return render(request, "project_info.html", context={"project": project})