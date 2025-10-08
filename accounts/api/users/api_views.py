from django.contrib.auth import get_user_model
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.viewsets import ModelViewSet

from accounts.api.users.serializers import UserModelSerializer
from utils.permissions import AdminOrOwner

User = get_user_model()


class UserModelViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserModelSerializer
    permission_classes = [AdminOrOwner]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['role']
