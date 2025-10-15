from django.db import models

from library.choices import NotificationTypeChoices


class Notification(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    user = models.ForeignKey('accounts.User', on_delete=models.CASCADE)
    is_read = models.BooleanField(default=False)
    type = models.CharField(max_length=10, choices=NotificationTypeChoices.choices,
                            default=NotificationTypeChoices.INFO)

    def __str__(self):
        return self.title
