from django.contrib.auth import get_user_model
from rest_framework.generics import UpdateAPIView, RetrieveAPIView
from rest_framework.permissions import IsAuthenticated

from accounts.api.me.serializers import ReadMeSerializer, WriteMeSerializer
from library.exceptions import UserNotFound

User = get_user_model()


class MeApi(UpdateAPIView, RetrieveAPIView):
    queryset = User.objects.all()
    permission_classes = [IsAuthenticated]
    http_method_names = ["get", "patch", "put"]
    lookup_field = "id"

    def get_object(self):
        user: User = self.queryset.filter(id=self.request.user.id).first()
        if user is None:
            raise UserNotFound
        return user

    def get_serializer_class(self):
        serializer_class = super().get_serializer_class()
        match self.request.method.lower():
            case "get":
                serializer_class = ReadMeSerializer
            case "patch" | "pit":
                serializer_class = WriteMeSerializer
        return serializer_class
