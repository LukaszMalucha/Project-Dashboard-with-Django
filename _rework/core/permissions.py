from rest_framework.permissions import BasePermission, SAFE_METHODS
from django.shortcuts import get_object_or_404
from core.models import MyProfile
from core.models_project import ProjectModel, IssueModel

class IsAdminOrReadOnly(BasePermission):
    """Allows only is_superuser users"""

    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True

        return request.user and request.user.is_superuser

class IsAdminOrReadAndCreateOnly(BasePermission):
    """Only superuser can delete or modify"""

    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True
        if request.method == "POST":
            return True

        return request.user and request.user.is_superuser



class IsOwnerOrReadOnly(BasePermission):
    """PM can only access"""
    def has_permission(self, request, view):
        pk=view.kwargs['pk']
        project = get_object_or_404(ProjectModel, id=pk)
        return project.proposed_by == request.user

class IsFixingOrReadOnly(BasePermission):
    """Only Coder that is fixing project issue can access that view"""
    def has_permission(self, request, view):
        pk=view.kwargs['id']
        issue = get_object_or_404(IssueModel, id=pk)
        return issue.assigned_to == request.user




