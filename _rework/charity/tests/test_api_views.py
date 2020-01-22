from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.test import APIClient

from charity import serializers
from core import models_charity
from core import models

CHARITIES_URL = reverse("charity:charities-list")
CHARITY_URL = reverse("charity:charities-detail", args=[1])
DONATE_URL = reverse("charity:donate")


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


def sample_charity():
    payload = {"name": "Test", "description": "test"}
    charity = models_charity.CharityModel.objects.create(**payload)
    return charity


def sample_donation(donor, charity):
    payload = {"donor": donor, "charity": charity}
    donation = models_charity.DonationModel.objects.create(**payload)
    return donation


class CharityApiTests(TestCase):
    """Test charity viewset"""

    def setUp(self):
        self.client = APIClient()
        self.user = sample_user()
        self.superuser = sample_superuser()
        self.charity = sample_charity()

    def test_retrieve_charities_list(self):
        """Test retrieving list of charities"""
        self.client.force_authenticate(self.user)
        charities = models_charity.CharityModel.objects.all()
        serializer = serializers.CharityModelSerializer(charities, many=True)
        response = self.client.get(CHARITIES_URL)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['count'], 1)

    def test_retrieve_charity(self):
        """Test retrieving single charity"""
        self.client.force_authenticate(self.user)
        response = self.client.get(CHARITY_URL)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_creating_charity_successful(self):
        """Test creating new charity"""
        self.client.force_authenticate(self.superuser)
        payload = {"name": "Test1", "description": "test1"}
        self.client.post(CHARITIES_URL, payload)
        exist = models_charity.CharityModel.objects.filter(
            name=payload['name'],
        ).exists()
        self.assertTrue(exist)

    def test_deleting_charity_successful(self):
        """Test deleting charity"""
        self.client.force_authenticate(self.superuser)
        response = self.client.delete(CHARITY_URL)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)


class DonationViewTests(TestCase):

    def setUp(self):
        self.client = APIClient()
        self.user = sample_user()
        self.superuser = sample_superuser()
        self.charity = sample_charity()
        self.donation = sample_donation(self.user, self.charity)

    def test_get_view(self):
        self.client.force_authenticate(self.user)
        response = self.client.get(DONATE_URL)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_donation(self):
        self.client.force_authenticate(self.superuser)
        payload = {"checkout": [1,]}
        response = self.client.post(DONATE_URL, payload)
        exist = models_charity.DonationModel.objects.filter(
            donor=self.superuser,
        ).exists()
        donations = models_charity.DonationModel.objects.all()
        profile = get_object_or_404(models.MyProfile, owner=self.superuser)
        self.assertEqual(profile.my_wallet, 995)
        self.assertEqual(len(donations), 2)
        self.assertTrue(exist)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_insufficient_coins(self):
        self.client.force_authenticate(self.user)
        payload = {"checkout": [1,]}
        response = self.client.post(DONATE_URL, payload)
        donations = models_charity.DonationModel.objects.all()
        profile = get_object_or_404(models.MyProfile, owner=self.user)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)