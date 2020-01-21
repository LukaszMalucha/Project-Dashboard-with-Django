from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient

from core.models import MyProfile

from user.api.views import ManageUserView

CREATE_USER_URL = reverse("api-user:create")
TOKEN_URL = reverse("api-user:authenticate")
MY_PROFILE_URL = reverse("api-user:my-profile")
CURRENT_USER_URL = reverse("api-user:current-user")
CURRENT_POSITION_URL = reverse("api-user:current-position")


def create_user(**params):
    return get_user_model().objects.create_user(**params)


class PublicUserApiTests(TestCase):
    """Test API requests that don't require authentication"""

    def setUp(self):
        self.client = APIClient()

    def test_create_valid_user_success(self):
        """Test creating user with valid payload is successful"""
        payload = {
            "email": "test@gmail.com",
            "password": "test1234",
            "name": "Test name"
        }

        response = self.client.post(CREATE_USER_URL, payload)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        user = get_user_model().objects.get(**response.data)
        self.assertTrue(user.check_password(payload["password"]))
        self.assertNotIn("password", response.data)

    def test_user_exists(self):
        """Test if creating user that already exists fails"""
        payload = {
            "email": "test@gmail.com",
            "password": "test1234",
            "name": "Test name"
        }
        create_user(**payload)

        response = self.client.post(CREATE_USER_URL, payload)

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_password_too_short(self):
        """Test if password is at least 8 characters"""
        payload = {
            "email": "test@gmail.com",
            "password": "test",
            "name": "Test name"
        }
        response = self.client.post(CREATE_USER_URL, payload)

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        user_exists = get_user_model().objects.filter(
            email=payload["email"]
        ).exists()
        self.assertFalse(user_exists)

    def test_create_token_for_user(self):
        """Test that token is created for the user"""
        payload = {
            "email": "test@gmail.com",
            "password": "test1234",
            "name": "Test name"
        }
        create_user(**payload)
        response = self.client.post(TOKEN_URL, payload)
        self.assertIn("token", response.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_token_invalid_credentials(self):
        """Test that token is not created if invalid credentials are given"""
        create_user(email="test@gmail.com", password="test1234")
        payload = {"email": "test@gmail.com", "password": "wrongpassword"}
        response = self.client.post(TOKEN_URL, payload)

        self.assertNotIn("token", response.data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_token_no_user(self):
        """Test that token is not created if user doesn't exist"""
        payload = {
            "email": "test@gmail.com",
            "password": "test1234",
            "name": "Test name"
        }
        response = self.client.post(TOKEN_URL, payload)

        self.assertNotIn("token", response.data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_token_missing_field(self):
        """Test that email and password are required"""
        response = self.client.post(TOKEN_URL, {"email": "one", "password": ""})

        self.assertNotIn("token", response.data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_retrieve_user_unauthorized(self):
        """Test that authentication is required for users"""
        response = self.client.get(MY_PROFILE_URL)

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)


class PrivateUserApiTests(TestCase):
    """Test API requests that require authentication"""

    def setUp(self):
        self.user = create_user(
            email="test@gmail.com",
            password="test1234",
            name="Test Name"
        )
        self.client = APIClient()
        self.client.force_authenticate(user=self.user)

    def test_retrieve_profile_success(self):
        """Test retrieving profile for logged in user"""
        response = self.client.get(MY_PROFILE_URL)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, {
            "name": self.user.name,
            "email": self.user.email
        })

    def test_get_object(self):
        """Test retrieve and return authenticated user"""
        view = ManageUserView()
        request = self.client.get(MY_PROFILE_URL)
        request.user = self.user
        view.request = request

        self.assertEqual(view.get_object(), self.user)

    def test_post_my_profile_not_allowed(self):
        """Test that POST is not allowed on the my profile url"""
        response = self.client.post(MY_PROFILE_URL, {})

        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)

    def test_update_user_profile(self):
        """Test updating the user profile for authenticated user"""
        payload = {
            "email": "test1@gmail.com",
            "password": "test123456",
            "name": "Test name 1"
        }

        response = self.client.patch(MY_PROFILE_URL, payload)

        self.user.refresh_from_db()
        self.assertEqual(self.user.name, payload['name'])
        self.assertTrue(self.user.check_password(payload['password']))
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class CurrentUserViewTests(TestCase):

    def setUp(self):
        self.user = create_user(
            email="test@gmail.com",
            password="test1234",
            name="Test Name"
        )
        self.client = APIClient()
        self.client.force_authenticate(user=self.user)

    def test_retrieve_current_user_success(self):
        """Test retrieving current user info"""

        response = self.client.get(CURRENT_USER_URL)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

class CurrentPositionViewTests(TestCase):

    def setUp(self):
        self.user = create_user(
            email="test@gmail.com",
            password="test1234",
            name="Test Name"
        )
        self.client = APIClient()
        self.client.force_authenticate(user=self.user)

    def test_retrieve_current_user_position(self):
        """Test retrieving current user position"""

        response = self.client.get(CURRENT_POSITION_URL)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, {
            "position": "guest",
        })






