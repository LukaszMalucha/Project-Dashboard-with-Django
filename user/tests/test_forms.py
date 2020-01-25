from django.contrib.auth import get_user_model
from django.test import TestCase

from user.forms import UserLoginForm, UserRegistrationForm, MyProfileForm


class UserLoginFormTests(TestCase):

    def setUp(self):
        self.user = get_user_model().objects.create_user(
            email="test@gmail.com",
            password="test1234",
            name="Test User"
        )

    def tearDown(self):
        self.user.delete()

    def test_valid_form(self):
        """Test valid form"""
        form = UserLoginForm({
            "email": "test@gmail.com",
            "password": "test1234"
        })
        self.assertTrue(form.is_valid())

    def test_email_missing(self):
        """Test user submits empty email"""
        form = UserLoginForm({
            "email": "",
            "password": "test1234"
        })
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['email'], [u'This field is required.'])

    def test_password_missing(self):
        """Test user submits empty password"""
        form = UserLoginForm({
            "email": "test@gmail.com",
            "password": ""
        })
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['password'], [u'This field is required.'])


class UserRegistrationFormTests(TestCase):

    def setUp(self):
        self.user = get_user_model().objects.create_user(
            email="test@gmail.com",
            password="test1234",
            name="Test User"
        )

    def tearDown(self):
        self.user.delete()

    def test_valid_form(self):
        """Test valid form"""
        form = UserRegistrationForm({
            "email": "tester@gmail.com",
            "name": "Test User",
            "password1": "test@1234",
            "password2": "test@1234"
        })
        self.assertTrue(form.is_valid())

    def test_email_missing(self):
        """Test user submits empty email"""
        form = UserRegistrationForm({
            "email": "",
            "name": "Test User",
            "password1": "test@1234",
            "password2": "test@1234"
        })
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['email'], [u'This field is required.'])

    def test_name_missing(self):
        """Test user submits empty name"""
        form = UserRegistrationForm({
            "email": "tester@gmail.com",
            "name": "",
            "password1": "test@1234",
            "password2": "test@1234"
        })
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['name'], [u'This field is required.'])

    def test_password1_missing(self):
        """Test user submits empty password"""
        form = UserRegistrationForm({
            "email": "tester@gmail.com",
            "name": "Test User",
            "password1": "",
            "password2": ""
        })
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['password1'], [u'This field is required.'])

    def test_password_mismatch(self):
        """Test password fields mismatch"""
        form = UserRegistrationForm({
            "email": "tester@gmail.com",
            "name": "Test User",
            "password1": "testing123456",
            "password2": "123456testing"
        })
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['password2'], [u'Passwords do not match'])

    def test_unique_email(self):
        """Test email field """
        form = UserRegistrationForm({
            "email": "test@gmail.com",
            "name": "Test User",
            "password1": "testing123456",
            "password2": "123456testing"
        })
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['email'], ['Email addresses must be unique.'])


class MyProfileFormTests(TestCase):

    def setUp(self):
        self.user = get_user_model().objects.create_user(
            email="test@gmail.com",
            password="test1234",
            name="Test User"
        )

    def tearDown(self):
        self.user.delete()

    def test_valid_form(self):
        """Test valid form"""
        form = MyProfileForm({
            "position": "Tester",
            "image": "images/test.jpg"
        })
        self.assertTrue(form.is_valid())


    def test_empty_fields_form(self):
        """Test that fields are not required"""
        form = MyProfileForm({
            "position": "",
            "image": ""
        })
        self.assertTrue(form.is_valid())





