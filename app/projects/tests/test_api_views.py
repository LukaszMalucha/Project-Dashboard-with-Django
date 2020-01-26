from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.test import APIClient

from projects import serializers
from core import models_project
from core import models

PROJECTS_URL = reverse("projects:projects-list")
PROJECT_URL = reverse("projects:projects-detail", args=[1])
PROJECT_PHASE_URL = reverse("projects:project-phase", kwargs={"pk": 1})
COMPLETE_PROJECT_URL = reverse("projects:project-complete", kwargs={"pk": 1})
TEAM_REQUIREMENTS_URL = reverse("projects:team-requirements", kwargs={"pk": 1})
TEAM_JOIN_URL = reverse("projects:project-team", kwargs={"pk": 1})
TEAM_REJECT_URL = reverse("projects:team-reject", kwargs={"pk": 1, "id": 1})
ISSUE_CREATE_URL = reverse("projects:issue-create", kwargs={"pk": 1})
ISSUE_ASSIGN_URL = reverse("projects:issue-assign", kwargs={"id": 1})
ISSUE_FIXED_URL = reverse("projects:issue-fixed", kwargs={"id": 1})
ISSUE_COUNT_URL = reverse("projects:issue-count")


def sample_superuser():
    user = get_user_model().objects.create_superuser(
        email="superuser@gmail.com",
        password="test1234",
    )
    return user


def sample_user():
    user = get_user_model().objects.create_user(
        email="user@gmail.com",
        password="test1234",
    )
    return user


def sample_project(user):
    payload = {"name": "Test Project", "description": "test", "proposed_by": user}
    project = models_project.ProjectModel.objects.create(**payload)
    return project


def sample_team_membership(user, project):
    payload = {"member": user, "project": project, "committed_skill": "js"}
    tm = models_project.TeamMembershipModel.objects.create(**payload)
    return tm


def sample_issue(user, project):
    payload = {"name": "Test", "description": "test", "cost": 1, "project": project, "assigned_to": user}
    issue = models_project.IssueModel.objects.create(**payload)
    return issue


class ProjectModelViewTests(TestCase):

    def setUp(self):
        self.client = APIClient()
        self.user = sample_user()
        self.superuser = sample_superuser()
        self.project = sample_project(self.superuser)

    def test_retrieve_projects_list(self):
        """Test retrieving list of projects"""
        self.client.force_authenticate(self.superuser)
        projects = models_project.ProjectModel.objects.all()
        serializer = serializers.ProjectModelSerializer(projects, many=True)
        response = self.client.get(PROJECTS_URL)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["count"], 1)
        exist = models_project.ProjectModel.objects.filter(
            name="Test Project",
        ).exists()
        self.assertTrue(exist)

    def test_create_project_successful(self):
        """Test creating a new project"""
        self.client.force_authenticate(self.superuser)
        payload = {"name": "Test1", "description": "test1", "proposed_by": self.superuser}
        profile = get_object_or_404(models.MyProfile, owner=self.superuser)
        profile.my_wallet = 1000
        profile.save()
        response = self.client.post(PROJECTS_URL, payload)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        exist = models_project.ProjectModel.objects.filter(
            name="Test1",
        ).exists()
        self.assertTrue(exist)

    def test_create_project_insufficient_wallet(self):
        """Test creating a new project with no leancoins"""
        self.client.force_authenticate(self.superuser)
        payload = {"name": "Test1", "description": "test1", "proposed_by": self.superuser}
        profile = get_object_or_404(models.MyProfile, owner=self.superuser)
        profile.my_wallet = 10
        profile.save()
        response = self.client.post(PROJECTS_URL, payload)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

class TeamRequirementsViewsTests(TestCase):

    def setUp(self):
        self.client = APIClient()
        self.user = sample_user()
        self.superuser = sample_superuser()
        self.project = sample_project(self.superuser)

    def test_retrieve_team_requirements(self):
        """Test retrieving team requirements"""
        self.client.force_authenticate(self.superuser)
        response = self.client.get(TEAM_REQUIREMENTS_URL)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_modifying_team_requirements(self):
        """Test modifying team requirements"""
        self.client.force_authenticate(self.superuser)
        payload = {"html": 1, "css": 1, "js": 1, "db": 1, "python": 1}
        response = self.client.put(TEAM_REQUIREMENTS_URL, payload)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_team_requirements_400(self):
        """Test modifying team requirements"""
        self.client.force_authenticate(self.superuser)
        payload = {"html": "asd", "css": 1, "js": 1, "db": 1, "python": 1}
        response = self.client.put(TEAM_REQUIREMENTS_URL, payload)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


class ProjectPhaseViewTests(TestCase):

    def setUp(self):
        self.client = APIClient()
        self.user = sample_user()
        self.superuser = sample_superuser()
        self.project = sample_project(self.superuser)

    def test_retrieve_project_phase(self):
        """Test retrieving project phase"""
        self.client.force_authenticate(self.superuser)
        response = self.client.get(PROJECT_PHASE_URL)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_changing_project_phase(self):
        """Test advancing project"""
        self.client.force_authenticate(self.superuser)
        payload = {"phase": "analysis"}
        response = self.client.patch(PROJECT_PHASE_URL, payload)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_changing_project_phase_400(self):
        """Test advancing project"""
        self.client.force_authenticate(self.superuser)
        payload = {"phase": 2}
        response = self.client.patch(PROJECT_PHASE_URL, payload)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


class ProjectCompleteViewTests(TestCase):

    def setUp(self):
        self.client = APIClient()
        self.user = sample_user()
        self.superuser = sample_superuser()
        self.project = sample_project(self.superuser)
        self.team_membership = sample_team_membership(self.user, self.project)

    def test_retrieve_completion_view(self):
        """Test get method"""
        self.client.force_authenticate(self.superuser)
        response = self.client.get(COMPLETE_PROJECT_URL)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_complete_project(self):
        """Test completing project"""
        self.client.force_authenticate(self.superuser)
        response = self.client.post(COMPLETE_PROJECT_URL)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)


class TeamJoinViewTests(TestCase):

    def setUp(self):
        self.client = APIClient()
        self.user = sample_user()
        self.superuser = sample_superuser()
        self.project = sample_project(self.superuser)

    def test_joining_team(self):
        """Test join team view"""
        self.client.force_authenticate(self.user)
        profile = get_object_or_404(models.MyProfile, owner=self.user)
        profile.position = "Coder"
        profile.personality = "achiever"
        profile.save()
        payload = {"committed_skill": "python"}
        response = self.client.post(TEAM_JOIN_URL, payload)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_joining_team_no_personality(self):
        """Test join team view"""
        self.client.force_authenticate(self.user)
        profile = get_object_or_404(models.MyProfile, owner=self.user)
        profile.position = "Coder"
        profile.save()
        payload = {"committed_skill": "python"}
        response = self.client.post(TEAM_JOIN_URL, payload)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_joining_team_second_time(self):
        """Test join team second time"""
        self.client.force_authenticate(self.user)
        profile = get_object_or_404(models.MyProfile, owner=self.user)
        profile.position = "Coder"
        profile.personality = "achiever"
        profile.save()
        payload = {"committed_skill": "python"}
        response = self.client.post(TEAM_JOIN_URL, payload)
        response_2 = self.client.post(TEAM_JOIN_URL, payload)
        self.assertEqual(response_2.status_code, status.HTTP_400_BAD_REQUEST)

    def test_joining_team_400(self):
        """Test join team view"""
        self.client.force_authenticate(self.user)
        profile = get_object_or_404(models.MyProfile, owner=self.user)
        profile.position = "Coder"
        profile.personality = "achiever"
        profile.save()
        payload = {"committed_skill": 12}
        response = self.client.post(TEAM_JOIN_URL, payload)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


class TeamRejectViewTests(TestCase):

    def setUp(self):
        self.client = APIClient()
        self.user = sample_user()
        self.superuser = sample_superuser()
        self.project = sample_project(self.superuser)
        self.team_membership = sample_team_membership(self.user, self.project)

    def test_retrieve_reject_view(self):
        """Test get method"""
        self.client.force_authenticate(self.superuser)
        response = self.client.get(TEAM_REJECT_URL)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_team_member(self):
        """Test removing team member"""
        self.client.force_authenticate(self.superuser)
        response = self.client.delete(TEAM_REJECT_URL)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_delete_non_exisiting_team_member(self):
        """Test removing team member"""
        self.client.force_authenticate(self.superuser)
        response = self.client.delete(reverse("projects:team-reject", kwargs={"pk": 1, "id": 3}))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)


class IssueCreateViewTests(TestCase):

    def setUp(self):
        self.client = APIClient()
        self.user = sample_user()
        self.superuser = sample_superuser()
        self.project = sample_project(self.superuser)
        self.issue = sample_issue(self.superuser, self.project)

    def test_retrieve_issue_create_view(self):
        """Test get method"""
        self.client.force_authenticate(self.superuser)
        response = self.client.get(ISSUE_CREATE_URL)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_issue_successful(self):
        """Test creating a new project issue"""
        self.client.force_authenticate(self.superuser)
        payload = {"name": "Test1", "description": "test1", "assigned_to": self.superuser, "cost": 12}
        response = self.client.post(ISSUE_CREATE_URL, payload)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        exist = models_project.IssueModel.objects.filter(
            name="Test1",
        ).exists()
        self.assertTrue(exist)

    def test_create_issue_400(self):
        """Test 400 response"""
        self.client.force_authenticate(self.superuser)
        payload = {"name": 123, "description": "test1", "assigned_to": "asd", "cost": "asd"}
        response = self.client.post(ISSUE_CREATE_URL, payload)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


class IssueAssignViewTests(TestCase):
    """Test assign issue views"""

    def setUp(self):
        self.client = APIClient()
        self.user = sample_user()
        self.superuser = sample_superuser()
        self.project = sample_project(self.superuser)
        self.issue = sample_issue(self.superuser, self.project)

    def test_retrieve_issue_assign_view(self):
        """Test get method"""
        self.client.force_authenticate(self.superuser)
        response = self.client.get(ISSUE_ASSIGN_URL)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_assign_to_new_user(self):
        """Test assigning to a new user"""
        self.client.force_authenticate(self.user)
        response = self.client.patch(ISSUE_ASSIGN_URL)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class IssueFixedViewTests(TestCase):
    """Testing issue fixed view"""

    def setUp(self):
        self.client = APIClient()
        self.user = sample_user()
        self.superuser = sample_superuser()
        self.project = sample_project(self.superuser)
        self.issue = sample_issue(self.superuser, self.project)

    def test_retrieve_issue_assign_view(self):
        """Test get method"""
        self.client.force_authenticate(self.superuser)
        response = self.client.get(ISSUE_FIXED_URL)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_issue_fixed_view(self):
        """Test issue fixed view"""
        self.client.force_authenticate(self.superuser)
        response = self.client.post(ISSUE_FIXED_URL)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class IssueCountViewTests(TestCase):
    """Testing issue count view"""

    def setUp(self):
        self.client = APIClient()
        self.user = sample_user()
        self.superuser = sample_superuser()
        self.project = sample_project(self.superuser)
        self.issue = sample_issue(self.superuser, self.project)

    def test_retrieve_issue_count_view(self):
        """Test get method"""
        self.client.force_authenticate(self.superuser)
        response = self.client.get(ISSUE_COUNT_URL)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
