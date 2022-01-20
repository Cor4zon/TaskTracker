import abc
import transaction as transaction
from tasks.models import Project, Task


class AbstractRepository(abc.ABC):

    @classmethod
    @abc.abstractmethod
    def create(cls, item):
        raise NotImplementedError

    @classmethod
    @abc.abstractmethod
    def read(cls, pk):
        raise NotImplementedError

    @classmethod
    @abc.abstractmethod
    def read_filtered(cls, filter_dict):
        raise NotImplementedError

    @classmethod
    @abc.abstractmethod
    def read_all(cls):
        raise NotImplementedError

    @classmethod
    @abc.abstractmethod
    def delete(cls, pk):
        raise NotImplementedError

    @classmethod
    @abc.abstractmethod
    def update(cls, pk, data):
        raise NotImplementedError


class ProjectRepository(AbstractRepository):
    @classmethod
    def create(cls, project_data):
        project = Project(
                            title=project_data["title"],
                            description=project_data["description"],
                            deadline=project_data["deadline"]
                         )
        project.save()

    @classmethod
    def read(cls, pk):
        return Project.objects.filter(pk=pk)

    @classmethod
    def read_filtered(cls, filter_dict):
        pass

    @classmethod
    def read_all(cls):
        return Project.objects.all()

    @classmethod
    def delete(cls, pk):
        Project.objects.filter(pk=pk).delete()

    @classmethod
    def update(cls, pk, data):
        Project.objects.filter(pk=pk).update(**data)


class TaskRepository(AbstractRepository):
    @classmethod
    def create(cls, task_info):
        task = Task(
                    title=task_info["title"],
                    description=task_info["description"],
                    status=task_info["status"],
                    deadline=task_info["deadline"],
                    project_id=task_info["project"]
                    )
        task.save()

    @classmethod
    def read(cls, task_pk):
        return Task.objects.filter(pk=task_pk)

    @classmethod
    def read_filtered(cls, filter_dict):
        return Task.objects.filter(**filter_dict)

    @classmethod
    def read_all(cls):
        return Task.objects.all()

    @classmethod
    def delete(cls, task_pk):
        Task.objects.filter(pk=task_pk).delete()

    @classmethod
    def update(cls, pk, data):
        pass



class CustomService():
    def __init__(self, repository):
        self.repository = repository

    def create(self, model):
        self.repository.create(model)

    def read(self, pk):
        return self.repository.read(pk)

    def read_filtered(self, project_pk):
        return self.repository.read_filtered(project_pk)

    def read_all(self):
        return self.repository.read_all()

    def delete(self, pk):
        return self.repository.delete(pk)

    def update(self, pk, data):
        return self.repository.update(pk, data)


ProjectService = CustomService(ProjectRepository)
TaskService = CustomService(TaskRepository)