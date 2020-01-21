# from django.contrib.auth import get_user_model
# from django.test import TestCase
# from django.urls import reverse
# from rest_framework import status
# from rest_framework.test import APIClient
# from django.shortcuts import get_object_or_404
# from core.permissions import IsAdminOrReadOnly, IsOwnerOrReadOnly, IsFixingOrReadOnly, IsAdminOrReadAndCreateOnly
# from core.models import MyProfile
# from core.models_project import ProjectModel, IssueModel
#
# CHARITIES_URL = reverse("charity:charities-list")
# PROJECTS_URL = reverse("projects:projects-list")
# TEAM_REQUIREMENTS_URL = reverse("projects:team-requirements", kwargs={'pk': 1})
# ISSUE_FIXED_URL = reverse("projects:issue-fixed", kwargs={'id': 1})
#
#
# class IsAdminOrReadOnlyTests(TestCase):
#
#     def setUp(self):
#         self.user = get_user_model().objects.create_user(
#             email="test@gmail.com",
#             password="test1234",
#             name="Test User"
#         )
#
#         self.user_superuser = get_user_model().objects.create_superuser(
#             email="superuser@gmail.com",
#             password="test1234",
#         )
#         self.charity_payload = {"name": "Test", "description": "test"}
#         self.permission = IsAdminOrReadOnly()
#
#     def test_superuser_has_admin_or_read_only_permission(self):
#         admin_permission = self.user_superuser.has_perm(IsAdminOrReadOnly)
#         self.assertTrue(admin_permission)
#
#     def test_user_has_no_admin_or_read_only_permission(self):
#         admin_permission = self.user.has_perm(IsAdminOrReadOnly)
#         self.assertFalse(admin_permission)
#
#     def test_user_cant_access_unsafe_methods(self):
#         payload = self.charity_payload
#         self.client = APIClient()
#         self.client.force_authenticate(user=self.user)
#         response = self.client.post(CHARITIES_URL, payload)
#         self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
#
#     def test_user_can_access_safe_methods(self):
#         self.client = APIClient()
#         self.client.force_authenticate(user=self.user)
#         response = self.client.get(CHARITIES_URL)
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
#
#     def test_superuser_can_access_unsafe_methods(self):
#         payload = self.charity_payload
#         self.client = APIClient()
#         self.client.force_authenticate(user=self.user_superuser)
#         response = self.client.post(CHARITIES_URL, payload)
#         self.assertEqual(response.status_code, status.HTTP_201_CREATED)
#
#
# class IsAdminOrReadAndCreateOnlyTests(TestCase):
#
#     def setUp(self):
#         self.user = get_user_model().objects.create_user(
#             email="test@gmail.com",
#             password="test1234",
#             name="Test User"
#         )
#
#         self.user_superuser = get_user_model().objects.create_superuser(
#             email="superuser@gmail.com",
#             password="test1234",
#         )
#         self.project_payload = {"name": "Test", "description": "test", "proposed_by": self.user}
#         self.permission = IsAdminOrReadAndCreateOnly()
#
#     def test_superuser_has_admin_or_read_and_create_only_permission(self):
#         admin_permission = self.user_superuser.has_perm(IsAdminOrReadAndCreateOnly)
#         self.assertTrue(admin_permission)
#
#     def test_user_can_access_safe_methods(self):
#         self.client = APIClient()
#         self.client.force_authenticate(user=self.user)
#         response = self.client.get(PROJECTS_URL)
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
#
#     def test_user_can_access_create_method(self):
#         payload = self.project_payload
#         profile = get_object_or_404(MyProfile, owner=self.user)
#         profile.my_wallet = 1000
#         profile.save()
#         self.client = APIClient()
#         self.client.force_authenticate(user=self.user)
#         response = self.client.post(PROJECTS_URL, payload)
#         self.assertEqual(response.status_code, status.HTTP_201_CREATED)
#
#     def test_user_cant_access_delete_method(self):
#         payload = self.project_payload
#         profile = get_object_or_404(MyProfile, owner=self.user)
#         profile.my_wallet = 1000
#         profile.save()
#         self.client = APIClient()
#         self.client.force_authenticate(user=self.user)
#         response = self.client.delete(PROJECTS_URL, payload)
#         self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
#
#
# class IsOwnerOrReadOnlyTests(TestCase):
#
#     def setUp(self):
#         self.user = get_user_model().objects.create_user(
#             email="test@gmail.com",
#             password="test1234",
#             name="Test User"
#         )
#
#         self.user_superuser = get_user_model().objects.create_superuser(
#             email="superuser@gmail.com",
#             password="test1234",
#         )
#         self.project_payload = {"name": "Test", "description": "test", "proposed_by": self.user}
#         self.permission = IsOwnerOrReadOnly()
#         self.project = ProjectModel.objects.create(name="Test", description="test", proposed_by=self.user)
#
#     def test_owner_can_access_view(self):
#         self.client = APIClient()
#         self.client.force_authenticate(user=self.user)
#         response = self.client.get(TEAM_REQUIREMENTS_URL)
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
#
#     def test_nonowner_cant_access_view(self):
#         self.client = APIClient()
#         self.client.force_authenticate(user=self.user_superuser)
#         response = self.client.get(TEAM_REQUIREMENTS_URL)
#         self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
#
#
# class IsFixingOrReadOnlyTests(TestCase):
#
#     def setUp(self):
#         self.user = get_user_model().objects.create_user(
#             email="test@gmail.com",
#             password="test1234",
#             name="Test User"
#         )
#
#         self.user_superuser = get_user_model().objects.create_superuser(
#             email="superuser@gmail.com",
#             password="test1234",
#         )
#         self.project_payload = {"name": "Test", "description": "test", "proposed_by": self.user}
#         self.permission = IsOwnerOrReadOnly()
#         self.project = ProjectModel.objects.create(name="Test", description="test", proposed_by=self.user)
#         self.issue = IssueModel.objects.create(name="Test", description="test", cost=12, project=self.project,
#                                               assigned_to=self.user)
#
#     def test_assignee_can_access_view(self):
#         self.client = APIClient()
#         self.client.force_authenticate(user=self.user)
#         response = self.client.get(ISSUE_FIXED_URL)
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
#
#     def test_random_user_cant_access_view(self):
#         self.client = APIClient()
#         self.client.force_authenticate(user=self.user_superuser)
#         response = self.client.get(ISSUE_FIXED_URL)
#         self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)