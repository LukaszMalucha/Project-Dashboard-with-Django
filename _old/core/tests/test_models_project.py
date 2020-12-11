from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
from django.test import TestCase

from core import models_project
from core.models import MyProfile


class ProjectModelTest(TestCase):

    def setUp(self):
        self.user = get_user_model().objects.create_user(
            email="test@gmail.com",
            password="test1234",
            name="Test User"
        )

        self.project = models_project.ProjectModel.objects.create(name="Test", description="test",
                                                                  proposed_by=self.user)

    def tearDown(self):
        self.user.delete()
        self.project.delete()

    def test_creating_project(self):
        self.assertTrue(self.project)

    def test_project_str(self):
        self.assertEqual(str(self.project), "Test")

    def test_my_project_verbose_name(self):
        self.assertEqual(self.project._meta.verbose_name_plural, "Projects")

    def test_project_on_hold(self):
        self.project.budget = -10
        self.project.save()
        self.assertEqual(self.project.phase, "on hold")


class IssueModelTest(TestCase):

    def setUp(self):
        self.user = get_user_model().objects.create_user(
            email="test@gmail.com",
            password="test1234",
            name="Test User"
        )

        self.project = models_project.ProjectModel.objects.create(name="Test", description="test",
                                                                  proposed_by=self.user)
        self.issue = models_project.IssueModel.objects.create(name="Test Issue", description="test", cost=12,
                                                              project=self.project,
                                                              assigned_to=self.user)

    def tearDown(self):
        self.user.delete()
        self.project.delete()
        self.issue.delete()

    def test_creating_issue(self):
        self.assertTrue(self.issue)

    def test_issue_str(self):
        self.assertEqual(str(self.issue), "Test-Test Issue")

    def test_my_profile_verbose_name(self):
        self.assertEqual(self.issue._meta.verbose_name_plural, "Projects Issues")


class TeamRequirementsModelTests(TestCase):

    def setUp(self):
        self.user = get_user_model().objects.create_user(
            email="test@gmail.com",
            password="test1234",
            name="Test User"
        )

        self.project = models_project.ProjectModel.objects.create(name="Test", description="test",
                                                                  proposed_by=self.user)
        self.team = get_object_or_404(models_project.TeamRequirementsModel, project=self.project)

    def tearDown(self):
        self.user.delete()
        self.project.delete()
        self.team.delete()

    def test_issue_str(self):
        self.assertEqual(str(self.team), "Test")


class TeamMembershipModelTests(TestCase):

    def setUp(self):
        self.user = get_user_model().objects.create_user(
            email="test@gmail.com",
            password="test1234",
            name="Test User"
        )

        self.project = models_project.ProjectModel.objects.create(name="Test", description="test",
                                                                  proposed_by=self.user)
        self.team_member = models_project.TeamMembershipModel.objects.create( project=self.project, member=self.user,
                                             committed_skill="js")

    def tearDown(self):
        self.user.delete()
        self.project.delete()
        self.team_member.delete()

    def test_issue_str(self):
        self.assertEqual(str(self.team_member), "Test test@gmail.com js")

    def test_name_field(self):
        self.assertEqual(self.user.name, self.team_member.member_name)

    def test_portrait_field(self):
        my_profile = get_object_or_404(MyProfile, owner=self.user)
        self.assertEqual(my_profile.image.url, self.team_member.member_portrait)

    def test_personality_field(self):
        my_profile = get_object_or_404(MyProfile, owner=self.user)
        self.assertEqual(my_profile.personality, self.team_member.member_personality)


class ProjectMessageModelTests(TestCase):

    def setUp(self):
        self.user = get_user_model().objects.create_user(
            email="test@gmail.com",
            password="test1234",
            name="Test User"
        )

        self.project = models_project.ProjectModel.objects.create(name="Test", description="test",
                                                                  proposed_by=self.user)
        self.project_message = models_project.ProjectMessageModel.objects.create( project=self.project, message="Test")

    def tearDown(self):
        self.user.delete()
        self.project.delete()
        self.project_message.delete()


    def test_project_message_str(self):
        self.assertEqual(str(self.project_message), "Test")








