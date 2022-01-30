from django.contrib.auth.models import User
from django.test import TestCase
from django.utils import timezone

from .models import Project, Task, Comment
from .forms import ProjectForm, TaskForm, CommentForm


class ProjectTestCase(TestCase):
    def setUp(self):
        # self.user1 = User.objects.create_user(username="admin")
        Project.objects.create(
            title="Test Project",
            description="We are testing this",
            tasksCount=0,
            deadline=timezone.now())

    def test_project_is_posted(self):
        """Posts are created"""
        project1 = Project.objects.get(title="Test Project")
        self.assertEqual(project1.description, "We are testing this")

    def test_blank_form_data(self):
        form = ProjectForm({})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors, {
            'title': ['This field is required.'],
            'description': ['This field is required.'],
            'deadline': ['This field is required.'],
        })
