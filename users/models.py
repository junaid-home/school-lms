from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager


class CustomAccountManger(BaseUserManager):
    def create_superuser(self, email, user_name, first_name, last_name, password, **other_fields):
        other_fields.setdefault('is_staff', True)
        other_fields.setdefault('is_superuser', True)
        other_fields.setdefault('is_active', True)
        other_fields.setdefault('role', 'admin')

        if other_fields.get('is_staff') is not True:
            raise ValueError(
                'Superuser must be assigned to is_staff=True.')
        if other_fields.get('role') != 'Admin':
            raise ValueError(
                'Superuser must be assigned to role=Admin.')
        if other_fields.get('is_superuser') is not True:
            raise ValueError(
                'Superuser must be assigned to is_superuser=True.')

        return self.create_user(email, user_name, first_name, last_name, password, **other_fields)

    def create_user(self, email, user_name, first_name, last_name, password, **other_fields):
        if not email:
            raise ValueError('You must provide an email address')

        email = self.normalize_email(email)
        user = self.model(email=email, user_name=user_name,
                          first_name=first_name, last_name=last_name, **other_fields)
        user.set_password(password)
        user.save()
        return user


ROLE_CHOICES = (
    ("Student", "STUDENT"),
    ("Admin", "ADMIN"),
    ("Parent", "PARENT"),
)


class User(AbstractBaseUser, PermissionsMixin):
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    role = models.CharField(choices=ROLE_CHOICES,
                            max_length=15, default='Student')
    created_date = models.DateTimeField(default=timezone.now)

    user_name = models.CharField(max_length=40, unique=True)
    email = models.EmailField(unique=True)

    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)

    USERNAME_FIELD = 'user_name'
    REQUIRED_FIELDS = ['email', 'role', 'first_name', 'last_name']

    objects = CustomAccountManger()

    def get_email_field_name(self):
        return self.email

    def __str__(self):
        return self.user_name
