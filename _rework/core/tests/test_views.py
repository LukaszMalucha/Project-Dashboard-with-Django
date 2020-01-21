from django.test import TestCase, Client
from django.test.utils import override_settings
from core.views import IndexTemplateView

class IndexViewTests(TestCase):
    """Test main view"""

    def setUp(self):
        self.client = Client()

    @override_settings(DEBUG=True)
    def test_indexdev_template_user(self):
        """Test that index-dev.html is used when debug = True"""

        response = IndexTemplateView.get_template_names(self)
        self.assertEqual(response, "index-dev.html")

