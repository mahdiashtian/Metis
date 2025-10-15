from django.contrib.auth import get_user_model
from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver

from accounts.models.notifications import Notification
from accounts.services.notification import NotificationService
from library.choices import NotificationTypeChoices

User = get_user_model()

sms_service = NotificationService(type_='sms')
email_service = NotificationService(type_='email')


@receiver(post_save, sender=Notification)
def send_notification(sender, instance: Notification, created, **kwargs):
    if created:
        if instance.type == NotificationTypeChoices.WARNING:
            sms_service.send(to=instance.user.phone_number, message=instance.content)
        email_service.send(to=instance.user.email, message=instance.content)


@receiver(pre_save, sender=User)
def reset_phone_verification(sender, instance, **kwargs):
    if not instance.pk:
        return

    old_phone = sender.objects.filter(pk=instance.pk).only('phone_number').first()
    if old_phone and old_phone != instance.phone_number:
        instance.verify_phone_number = False
