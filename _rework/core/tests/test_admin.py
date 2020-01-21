# from django.contrib.auth import get_user_model
# from django.test import TestCase, Client
# from django.urls import reverse
#
#
# class AdminSiteTests(TestCase):
#
#     def setUp(self):
#         """Creating admin and spare user for testing"""
#         self.client = Client()
#         self.admin_user = get_user_model().objects.create_superuser(
#             email="admin@test.com",
#             password="test1234"
#         )
#         self.client.force_login(self.admin_user)  # helper function to log in user
#         self.user = get_user_model().objects.create_user(
#             email="test@gmail.com",
#             password="test1234",
#             name="Test User"
#         )
#
#     def tearDown(self):
#         self.admin_user.delete()
#         self.user.delete()
#
#     def test_users_listed(self):
#         """Test that users are listed on admin page"""
#         url = reverse('admin:core_user_changelist')  # url updates automatically with reverse
#         response = self.client.get(url)
#
#         self.assertContains(response, self.user.name)
#         self.assertContains(response, self.user.email)
#
#     def test_user_change_page(self):
#         """Test that the user edit page works"""
#         url = reverse('admin:core_user_change', args=[self.user.id])  # admin/core/user/1
#         response = self.client.get(url)
#
#         self.assertEqual(response.status_code, 200)
#
#     def test_create_user_page(self):
#         """Test that the create user page works"""
#         url = reverse('admin:core_user_add')
#         response = self.client.get(url)
#
#         self.assertEqual(response.status_code, 200)
