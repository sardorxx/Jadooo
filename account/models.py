from uuid import uuid4

from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.utils import timezone
from django.db import models


class DevicesLockUnlock(models.Model):
    device_id = models.IntegerField(primary_key=True)
    device_name = models.CharField(max_length=50)
    device_ip = models.CharField(max_length=15)
    is_locked = models.BooleanField(default=False)
    user_device = models.CharField(max_length=30)
    location = models.CharField(max_length=100)
    last_login = models.DateTimeField(auto_now=True)
    is_safe = models.CharField(max_length=5)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)


class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')

        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        return self.create_user(email, password, **extra_fields)


class CustomUser(AbstractBaseUser, PermissionsMixin):
    OPTION1 = 'Child'
    OPTION2 = 'Men'
    OPTION3 = 'Women'
    OPTION4 = 'No'

    CHOICES = [
        (OPTION1, 'Child'),
        (OPTION2, 'Men'),
        (OPTION3, 'Women'),
        (OPTION4, '-----')
    ]
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=20, unique=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    phone = models.CharField('Phone_number', max_length=13)
    image = models.ImageField(upload_to='users_image/')
    sex = models.CharField(
        max_length=10,
        choices=CHOICES,
        default=OPTION4,
    )
    birth_date = models.DateField(blank=True, null=True)
    address = models.TextField(max_length=255)
    job = models.CharField(max_length=20, blank=True, null=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    date_joined = models.DateTimeField(default=timezone.now)

    # Add your additional fields here

    objects = CustomUserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    def __str__(self):
        return self.username
