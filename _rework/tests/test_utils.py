from django.contrib.auth import get_user_model
from django.test import TestCase

from user.utils import compile_profile, personality_test as pt
from core.models import MyProfile


class CompileProfileTests(TestCase):

    def setUp(self):
        self.user = get_user_model().objects.create_user(
            email="test@gmail.com",
            password="test1234",
            name="Test User"
        )

        self.my_profile = MyProfile.objects.filter(owner__email="test@gmail.com").first()

    def tearDown(self):
        self.user.delete()
        self.my_profile.delete()

    def test_pm_position(self):
        profile = self.my_profile
        profile.position = "PM"
        profile.save()
        context = compile_profile(self.user)

        self.assertEqual(context["position"], "Project Manager")

    def test_admin_position(self):
        profile = self.my_profile
        profile.position = "admin"
        profile.save()
        context = compile_profile(self.user)

        self.assertEqual(context["position"], "Program Manager")

    def test_coder_position(self):
        profile = self.my_profile
        profile.position = "Coder"
        profile.save()
        context = compile_profile(self.user)

        self.assertEqual(context["position"], "Coder")


class PersonalityTests(TestCase):

    def test_zero_answers(self):
        answers = []
        personality = pt(answers)

        self.assertEqual(personality, "socializer")

    def test_killer_answers(self):
        answers = ["answer_3" for i in range(6)]
        personality = pt(answers)

        self.assertEqual(personality , "killer")
