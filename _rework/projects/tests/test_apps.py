from django.test import TestCase

from projects.apps import ProjectsConfig


class ProjectsConfigAppTests(TestCase):

    def test_app_name(self):
        self.assertEqual(ProjectsConfig.name, "projects")