from django.test import TestCase

from charity.apps import CharityConfig


class CharityConfigAppTests(TestCase):

    def test_app_name(self):
        self.assertEqual(CharityConfig.name, "charity")
