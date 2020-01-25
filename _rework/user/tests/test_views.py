from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
from django.contrib.messages import get_messages
from django.test import Client
from django.test import TestCase
from django.urls import reverse

from core.models import MyProfile
from user.utils import personality_test

CREATE_USER_URL = reverse("user:register")
LOGIN_USER_URL = reverse("user:login")
LOGOUT_USER_URL = reverse("user:logout")
MY_PROFILE_URL = reverse("user:profile")
EDIT_PROFILE_URL = reverse("user:edit_profile")
GAMIFICATION_TEST_URL = reverse("user:gamification_test")


def create_user(**params):
    return get_user_model().objects.create_user(**params)


class RegisterUserTests(TestCase):
    """Test register user view"""

    def setUp(self):
        self.client = Client()

    def test_get_register_page(self):
        """Test that login page is accessible"""
        response = self.client.get(CREATE_USER_URL)
        self.assertEqual(response.status_code, 200)

    def test_create_valid_user_success(self):
        """Test creating user with valid payload is successful"""

        payload = {
            "email": "test@gmail.com",
            "password1": "test@1234567",
            "password2": "test@1234567",
            "name": "Test name"
        }

        response = self.client.post(CREATE_USER_URL, payload)
        self.assertEqual(response.status_code, 302)
        user_exists = get_user_model().objects.filter(email=payload["email"]).exists()
        self.assertTrue(user_exists)
        user_profile_exists = MyProfile.objects.filter(owner__email="test@gmail.com").exists()
        self.assertTrue(user_profile_exists)
        self.assertEqual(response['Location'], "/")
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(str(messages[0]), "You have successfully registered")


class LoginUserTests(TestCase):
    """Test login user view"""

    def setUp(self):
        self.client = Client()

    def test_get_login_page(self):
        """Test that register page is accessible"""
        response = self.client.get(LOGIN_USER_URL)
        self.assertEqual(response.status_code, 200)

    def test_login_valid_user_success(self):
        """Test login user with valid payload is successful"""

        payload = {
            "email": "test@gmail.com",
            "password": "test@1234567",
            "name": "Test name"
        }

        create_user(**payload)

        response = self.client.post(LOGIN_USER_URL, payload)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response['Location'], "/")
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(str(messages[0]), "You have successfully logged in")

    def test_login_invalid_credentials_user(self):
        """Test login user with invalid credentials"""

        payload = {
            "email": "test@gmail.com",
            "password": "test@1234567",
            "name": "Test name"
        }

        payload_invalid = {
            "email": "invalid@gmail.com",
            "password": "test@1234567",
            "name": "Test name"
        }

        create_user(**payload)
        response = self.client.post(LOGIN_USER_URL, payload_invalid)
        self.assertEqual(response.status_code, 200)
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(str(messages[0]), "Incorrect username or password")

    def test_user_can_login(self):
        payload = {
            "email": "test@gmail.com",
            "password": "test@1234567",
            "name": "Test name"
        }

        auth_user = create_user(**payload)
        self.client.login(email=payload['email'], password=payload['password'])
        response = self.client.get('/')


class LogoutUserTests(TestCase):

    def setUp(self):
        self.user = create_user(
            email="test@gmail.com",
            password="test1234",
            name="Test Name"
        )

        self.client = Client()
        self.client.force_login(self.user)

    def test_logout_redirects(self):
        response = self.client.get(LOGOUT_USER_URL)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response['Location'], "/")
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(str(messages[0]), "You have successfully logged out")


class UserProfileTests(TestCase):

    def setUp(self):
        self.user = create_user(
            email="test@gmail.com",
            password="test1234",
            name="Test Name"
        )

        self.client = Client()

    def test_retrieve_user_profile(self):
        self.client.force_login(self.user)
        response = self.client.get(MY_PROFILE_URL)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "profile.html")

    def test_retrieve_profile_unauthorized(self):
        response = self.client.get(MY_PROFILE_URL)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response['Location'], "/user/login?next=/user/profile")


class EditUserProfileTests(TestCase):

    def setUp(self):
        self.user = create_user(
            email="test@gmail.com",
            password="test1234",
            name="Test Name"
        )

        self.client = Client()
        self.my_profile = get_object_or_404(MyProfile, owner=self.user)

    def test_retrieving_edit_profile_page(self):
        """Test retrieving profile page"""
        self.client.force_login(self.user)
        response = self.client.get(EDIT_PROFILE_URL)
        self.assertEqual(response.status_code, 200)

    def test_edit_user_profile(self):
        """Test editing user own profile"""
        payload = {
            "position": "coder",
            "image": "portraits/tests.jpg",
        }

        self.assertTrue(self.my_profile)
        self.client.force_login(self.user)
        response = self.client.post(EDIT_PROFILE_URL, payload)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response['Location'], "/user/profile")

    def test_pm_wallet(self):
        """Test if PM receives 500 Leancoins at the start"""
        payload = {
            "position": "PM",
        }
        self.assertTrue(self.my_profile)
        self.client.force_login(self.user)
        self.client.post(EDIT_PROFILE_URL, payload)
        profile = get_object_or_404(MyProfile, owner=self.user)
        self.assertEqual(profile.my_wallet, 500)

    def test_coder_wallet(self):
        """Test if PM receives 500 Leancoins at the start"""
        payload = {
            "position": "Coder",
        }
        self.assertTrue(self.my_profile)
        self.client.force_login(self.user)
        self.client.post(EDIT_PROFILE_URL, payload)
        profile = get_object_or_404(MyProfile, owner=self.user)
        self.assertEqual(profile.my_wallet, 100)


class GamificationViewTests(TestCase):

    def setUp(self):
        self.user = create_user(
            email="test@gmail.com",
            password="test1234",
            name="Test Name"
        )

        self.client = Client()
        self.client.force_login(self.user)
        self.profile = get_object_or_404(MyProfile, owner=self.user)
        answers = ["answer_1" for i in range(6)]

    def test_retrieving_gamification_test_page(self):
        response = self.client.get(GAMIFICATION_TEST_URL)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "gamification_test.html")

    def test_passing_test_answers(self):
        payload = {
            "question_1": "answer_1", "question_2": "answer_1", "question_3": "answer_1",
            "question_4": "answer_1", "question_5": "answer_1", "question_6": "answer_1",
        }
        response = self.client.post(GAMIFICATION_TEST_URL, payload)
        self.assertEqual(response.status_code, 302)
