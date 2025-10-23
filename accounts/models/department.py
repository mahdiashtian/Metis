from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Department(models.Model):
    owner = models.ForeignKey(User, related_name='owner_departments', on_delete=models.CASCADE)
    users = models.ManyToManyField(User, related_name='user_departments')
    title = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField()

    def __str__(self):
        return self.title
