from django.db import models

class NotificationTypeChoices(models.TextChoices):
    INFO = 'info'
    WARNING = 'warning'
    ERROR = 'error'



class UserRoleChoices(models.TextChoices):
    EMPLOYEE = 'EMPLOYEE'
    HR = 'HR'
    ADMIN = 'ADMIN'
