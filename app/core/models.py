from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models
from core.utils import content_file_name
from django.contrib.auth.models import User



class MyProfile(models.Model):
    """User Profile Details"""
    position = models.CharField(max_length=254, default='guest', blank=True)
    personality = models.CharField(max_length=254, default='', blank=True)
    image = models.ImageField(upload_to=content_file_name, default='portraits/default.jpg')
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    my_wallet = models.DecimalField(max_digits=6, decimal_places=0, default=0)

    def save(self, *args, **kwargs):
        if self.position == "PM" and self.my_wallet == 0:
            self.my_wallet = 500
        if self.position == "Coder" and self.my_wallet == 0:
            self.my_wallet = 100
        super(MyProfile, self).save(*args, **kwargs)

    class Meta:
        verbose_name = "User Profile"
        verbose_name_plural = "User Profiles"

    def __str__(self):
        return str(self.owner) + " profile"