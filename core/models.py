from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.urls import reverse


class UserManager(BaseUserManager):

    def create_user(self, email, password=None, **extra_fields):
        """Create and save new user"""
        if not email:
            raise ValueError('User must have a valid email address')
        user = self.model(email=self.normalize_email(email), **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password):
        user = self.create_user(email, password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)

        return user


class User(AbstractBaseUser, PermissionsMixin):
    """Customized user model that allows using email instead of username"""
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'


class MyProfile(models.Model):
    """User Profile Details"""
    position = models.CharField(max_length=254, default='Coder', blank=True)
    personality = models.CharField(max_length=254, default='', blank=True)
    image = models.ImageField(upload_to='portraits/', default='portraits/default.jpg')
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    my_wallet = models.DecimalField(max_digits=6, decimal_places=0, default=0)

    class Meta:
        verbose_name = "User Profile"
        verbose_name_plural = "User Profiles"

    def get_absolute_url(self):
        return reverse('profile', kwargs={'pk': self.pk})

    def __str__(self):
        return str(self.owner)


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



