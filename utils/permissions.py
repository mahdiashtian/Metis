from rest_framework.permissions import BasePermission, SAFE_METHODS

from utils.type import RoleChoices


class AdminOrSafeMethodsReadOnly(BasePermission):
    def has_permission(self, request, view):
        user = request.user
        if user.role == RoleChoices.ADMIN.value or request.method in SAFE_METHODS:
            return True
        return False


class AdminOrOwner(BasePermission):
    def has_permission(self, request, view):
        user = request.user
        if user.role == RoleChoices.ADMIN.value:
            return True
        return False

    def has_object_permission(self, request, view, obj):
        user = request.user
        if user == obj or user.role == RoleChoices.ADMIN.value:
            return True
        return False
