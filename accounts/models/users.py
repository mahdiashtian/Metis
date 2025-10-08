from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    class RoleChoices(models.TextChoices):
        EMPLOYEE = 'EMPLOYEE'
        HR = 'HR'
        ADMIN = 'ADMIN'

    role = models.CharField(choices=RoleChoices.choices, default=RoleChoices.EMPLOYEE.value)
    phone_number = models.CharField(max_length=13, unique=True)
    is_superuser = None
    is_staff = None
