from django.test import TestCase

from core.apps import CoreConfig


class CoreConfigAppTests(TestCase):

    def test_app_name(self):
        self.assertEqual(CoreConfig.name, "core")
