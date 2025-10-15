from django.contrib.auth.models import AbstractUser
from django.db import models
from redis.commands.helpers import random_string

from library.choices import UserRoleChoices


class User(AbstractUser):
    role = models.CharField(choices=
                            UserRoleChoices.choices, default=UserRoleChoices.EMPLOYEE.value)
    phone_number = models.CharField(max_length=13, unique=True)
    verify_phone_number = models.BooleanField(default=False)
    code = models.CharField(default=random_string, max_length=10, unique=True, editable=False)
    image = models.ImageField(null=True, blank=True)

    is_superuser = None
    is_staff = None
