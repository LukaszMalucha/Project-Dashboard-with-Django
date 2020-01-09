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
        MyProfile.objects.get_or_create(owner=self, position="admin")

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

    # Add AUTH_USER_MODEL to settings !!!


class MyProfile(models.Model):
    """User Profile Details"""
    position = models.CharField(max_length=254, default='Coder', blank=True)
    personality = models.CharField(max_length=254, default='', blank=True)
    image = models.ImageField(upload_to=content_file_name, default='portraits/default.jpg')
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    my_wallet = models.DecimalField(max_digits=6, decimal_places=0, default=0)

    class Meta:
        verbose_name = "User Profile"
        verbose_name_plural = "User Profiles"

    def get_absolute_url(self):
        return reverse('profile', kwargs={'pk': self.pk})

    def __str__(self):
        return str(self.owner) + " profile"


class Position(models.Model):
    """Company Positions"""
    name = models.CharField(max_length=254, default='undefined')

    class Meta:
        verbose_name = "Company Position"
        verbose_name_plural = "Company Positions"

    def __str__(self):
        return self.name


class Personality(models.Model):
    """Personality Test outcome"""
    name = models.CharField(max_length=254, default='undefined')

    class Meta:
        verbose_name = "Personality Type"
        verbose_name_plural = "Personality Types"

    def __str__(self):
        return self.name
