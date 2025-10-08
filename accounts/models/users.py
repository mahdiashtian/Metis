from django.contrib.auth.models import AbstractUser
from django.db import models

from utils.type import RoleChoices


class User(AbstractUser):


    role = models.CharField(choices=
                            RoleChoices.choices, default=RoleChoices.EMPLOYEE.value)
    phone_number = models.CharField(max_length=13, unique=True)
    is_superuser = None
    is_staff = None
