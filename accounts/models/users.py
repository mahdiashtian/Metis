from django.contrib.auth.models import AbstractUser
from django.db import models
from redis.commands.helpers import random_string

from utils.type import RoleChoices


class User(AbstractUser):
    role = models.CharField(choices=
                            RoleChoices.choices, default=RoleChoices.EMPLOYEE.value)
    phone_number = models.CharField(max_length=13, unique=True)
    verify_phone_number = models.BooleanField(default=False)
    code = models.CharField(default=random_string, max_length=10, unique=True, editable=False)
    image = models.ImageField(null=True, blank=True)

    is_superuser = None
    is_staff = None
