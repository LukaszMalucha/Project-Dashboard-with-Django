from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models
from core.utils import content_file_name


# Manager Class
class UserManager(BaseUserManager):

    # extra fields in case we want to extend class in a future
    def create_user(self, email, password=None, **extra_fields):
        """Creates and saves a new user"""
        if not email:
            raise ValueError('Users must have an email address')
        if len(str(password)) < 8:
            raise ValueError('This password is too short. It must contain at least 8 characters.')
        user = self.model(email=self.normalize_email(email), **extra_fields)  # helper function to lowercase email
        user.set_password(password)  # hash helper function
        user.save(using=self._db)  # in case of multiple dbs
        return user

    # create superuser helper function
    def create_superuser(self, email, password):
        user = self.create_user(email, password)
        user.name = "Admin"
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)
        my_profile, created = MyProfile.objects.get_or_create(owner=user)
        my_profile.position = "admin"
        my_profile.my_wallet = 1000
        my_profile.save()

        return user


# Model Class
class User(AbstractBaseUser, PermissionsMixin):
    """Custom user model that allows using email instead of username"""
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    # Assign user manager to objects attribute
    objects = UserManager()

    USERNAME_FIELD = 'email'  # customize to email

    def save(self, *args, **kwargs):
        super(User, self).save(*args, **kwargs)
        MyProfile.objects.get_or_create(owner=self)


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