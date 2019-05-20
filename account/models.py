from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
)

# Create your models here.


class UserManager(BaseUserManager):
    def create_user(self, email, username, password):
        if not email:
            raise ValueError('An email is required for this user')
        if not password:
            raise ValueError('Please provide a password for this user')

        user = self.model(
            email=email
        )
        user.user_name = username
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_staff_user(self, email, username, password):
        user = self.create_user(email, username=username, password=password)
        user.is_staff = True
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, password):
        user = self.create_user(email, username=username, password=password)
        user.is_staff = True
        user.is_admin = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    email = models.EmailField(
        max_length=255,
        verbose_name='Email Address',
        unique=True
    )
    first_name = models.CharField(
        max_length=255,
        verbose_name='First name'
    )
    last_name = models.CharField(
        max_length=255,
        verbose_name='Last name'
    )
    user_name = models.CharField(
        max_length=255,
        verbose_name='Full name'
    )

    confirmed = models.BooleanField()
    date_joined = models.DateTimeField(auto_now_add=True)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def get_full_name(self):
        return self.first_name + ' ' + self.last_name

    def get_short_name(self):
        return self.first_name



