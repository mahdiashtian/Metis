from django.contrib.auth import get_user_model
from rest_framework import serializers

from accounts.api.me.serializers import ReadMeSerializer
from library.exceptions.conflict import PhoneAlreadyExists, EmailAlreadyExists
from django.forms import formset_factory
User = get_user_model()


class WriteMeSerializer(serializers.Serializer):
    first_name = serializers.CharField(required=False, allow_blank=True, max_length=150)
    last_name = serializers.CharField(required=False, allow_blank=True, max_length=150)
    phone_number = serializers.CharField(required=False, allow_blank=True, max_length=13)
    email = serializers.EmailField(required=False, allow_blank=True)
    image = serializers.ImageField(required=False, allow_null=True)

    def to_representation(self, instance):
        return ReadMeSerializer(instance).data

    def validate_phone_number(self, value):
        if User.objects.exclude(pk=self.instance.pk).filter(phone_number=value).exists():
            raise PhoneAlreadyExists
        return value

    def validate_email(self, value):
        if User.objects.exclude(pk=self.instance.pk).filter(email=value).exists():
            raise EmailAlreadyExists
        return value

    def update(self, instance, validated_data):
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save(update_fields=[
            "first_name",
            "last_name",
            "phone_number",
            "verify_phone_number",
            "email",
            "image",
        ])
        return instance
