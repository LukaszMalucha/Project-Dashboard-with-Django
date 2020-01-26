from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
from django.test import TestCase

from core import models_charity
from core.models import MyProfile


class CharityModelTests(TestCase):

    def setUp(self):
        self.charity = models_charity.CharityModel.objects.create(name="Test", description="test")

    def tearDown(self):
        self.charity.delete()

    def test_charity_str(self):
        self.assertEqual(str(self.charity), "Test")


class DonationModelTests(TestCase):

    def setUp(self):
        self.user = get_user_model().objects.create_user(
            email="test@gmail.com",
            password="test1234",
            name="Test User"
        )

        self.charity = models_charity.CharityModel.objects.create(name="Test", description="test")
        self.donation = models_charity.DonationModel.objects.create(donor=self.user, charity=self.charity)

    def tearDown(self):
        self.charity.delete()
        self.donation.delete()

    def test_donation_str(self):
        self.assertEqual(str(self.donation), "test@gmail.com - Test")
