from django.contrib.auth import get_user_model
from django.db.models.signals import pre_save
from django.dispatch import receiver

User = get_user_model()


@receiver(pre_save, sender=User)
def reset_phone_verification(sender, instance, **kwargs):
    if not instance.pk:
        return

    old_phone = sender.objects.filter(pk=instance.pk).only('phone_number').first()
    if old_phone and old_phone != instance.phone_number:
        instance.verify_phone_number = False
