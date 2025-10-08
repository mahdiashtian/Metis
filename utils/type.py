from django.db import models


class RoleChoices(models.TextChoices):
    EMPLOYEE = 'EMPLOYEE'
    HR = 'HR'
    ADMIN = 'ADMIN'
