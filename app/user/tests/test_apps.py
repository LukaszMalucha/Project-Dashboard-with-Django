from django.test import TestCase

from user.apps import UserConfig


class UserConfigAppTests(TestCase):

    def test_app_name(self):

        self.assertEqual(UserConfig.name, "user")