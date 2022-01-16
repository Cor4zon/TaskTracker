from tasks.models import Project, Task
from abc import ABCMeta, abstractmethod
from .db_manager import DBConfigManager


class Repository:

    __metaclass__ = ABCMeta
    db_config_manager = DBConfigManager()

    def create(self):
        pass