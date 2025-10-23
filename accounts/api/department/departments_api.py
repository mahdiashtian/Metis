from django.db.models import Q
from django_filters.rest_framework import DjangoFilterBackend
from drf_spectacular.utils import extend_schema, extend_schema_view, OpenApiParameter, OpenApiResponse
from rest_framework import mixins, status
from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import GenericViewSet

from accounts.api.department.serializers import ReadDepartmentSerializer
from accounts.models.departments import Department


@extend_schema_view(
    list=extend_schema(
        tags=["departments"],
        summary="List departments",
        description="Retrieve a list of departments with filtering, searching and ordering capabilities.",
        parameters=[
            OpenApiParameter(
                name="search",
                type=str,
                required=False,
                description="Search in department titles"
            ),
            OpenApiParameter(
                name="ordering",
                type=str,
                enum=["id", "-id", "title", "-title"],
                required=False,
                description="Ordering field (prefix with '-' for descending)"
            )
        ],
        responses={
            status.HTTP_200_OK: ReadDepartmentSerializer(many=True),
            status.HTTP_401_UNAUTHORIZED: OpenApiResponse(
                response={
                    "type": "object",
                    "properties": {
                        "detail": {
                            "type": "string",
                            "example": "Authentication credentials were not provided."
                        }
                    }
                },
                description="Authentication required."
            )
        }
    ),
    retrieve=extend_schema(
        tags=["departments"],
        summary="Retrieve department",
        description="Get detailed information about a specific department.",
        responses={
            status.HTTP_200_OK: ReadDepartmentSerializer,
            status.HTTP_401_UNAUTHORIZED: OpenApiResponse(
                response={
                    "type": "object",
                    "properties": {
                        "detail": {
                            "type": "string",
                            "example": "Authentication credentials were not provided."
                        }
                    }
                },
                description="Authentication required."
            ),
            status.HTTP_404_NOT_FOUND: OpenApiResponse(
                response={
                    "type": "object",
                    "properties": {
                        "detail": {
                            "type": "string",
                            "example": "Not found."
                        }
                    }
                },
                description="Department not found."
            )
        }
    )
)
class DepartmentApi(GenericViewSet, mixins.ListModelMixin, mixins.RetrieveModelMixin):
    serializer_class = ReadDepartmentSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [OrderingFilter, SearchFilter]
    ordering = ['id']
    search_fields = ['title']

    def get_queryset(self):
        user = self.request.user
        return Department.objects.select_related('owner').prefetch_related('users').filter(
            Q(owner=user) | Q(users=user)
        )
