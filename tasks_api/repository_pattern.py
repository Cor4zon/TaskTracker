import abc
from tasks.models import Project, Task
from django.shortcuts import get_object_or_404


class AbstractRepository(abc.ABC):

    @classmethod
    @abc.abstractmethod
    def add(cls, item):
        raise NotImplementedError

    @classmethod
    @abc.abstractmethod
    def get(cls, pk):
        raise NotImplementedError

    @classmethod
    @abc.abstractmethod
    def get_filtered(cls, filter_dict):
        raise NotImplementedError

    @classmethod
    @abc.abstractmethod
    def list(cls):
        raise NotImplementedError

    @classmethod
    @abc.abstractmethod
    def delete(cls, pk):
        raise NotImplementedError

    @classmethod
    @abc.abstractmethod
    def patch(cls):
        raise NotImplementedError


class ProjectRepository(AbstractRepository):
    @classmethod
    # @transaction.atomic
    def add(cls, project: Project):
        project.save()

    @classmethod
    def get(cls, pk):
        queryset = Project.objects.filter()
        return get_object_or_404(queryset, pk=pk)

    @classmethod
    def get_filtered(cls, filter_dict):
        pass

    @classmethod
    def list(cls):
        return Project.objects.all()

    @classmethod
    def delete(cls, pk):
        Project.objects.filter(pk=pk).delete()

    @classmethod
    def patch(cls):
        pass


class TaskRepository(AbstractRepository):
    @classmethod
    # @transaction.atomic
    def add(cls, task: Task):
        task.save()

    @classmethod
    def get(cls, task_pk):
        queryset = Task.objects.filter(pk=task_pk)
        return get_object_or_404(queryset, pk=task_pk)

    @classmethod
    def get_filtered(cls, filter_dict):
        return Task.objects.filter(**filter_dict)

    @classmethod
    def list(cls):
        return Task.objects.all()

    @classmethod
    def delete(cls, task_pk):
        Task.objects.filter(pk=task_pk).delete()

    @classmethod
    def patch(cls):
        pass


class CustomService():
    def __init__(self, repository):
        self.repository = repository

    def add(self, model):
        self.repository.add(model)

    def get(self, pk):
        return self.repository.get(pk)

    def get_filtered(self, project_pk):
        return self.repository.get_filtered(project_pk)

    def list(self):
        return self.repository.list()

    def delete(self, pk):
        return self.repository.delete(pk)

    def patch(self):
        pass


ProjectService = CustomService(ProjectRepository)
TaskService = CustomService(TaskRepository)