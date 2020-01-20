from rest_framework.permissions import BasePermission, SAFE_METHODS
from django.shortcuts import get_object_or_404
from core.models import MyProfile

class IsAdminOrReadOnly(BasePermission):
    """Allows only is_staff users"""

    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True

        return request.user and request.user.is_superuser

class IsManagerOrReadOnly(BasePermission):
    """PM can only create"""

    def has_permission(self, request, view):
        if request.method in SAFE_METHODS or request.method == "POST":
            return True
        if request.user.is_superuser:
            return True


