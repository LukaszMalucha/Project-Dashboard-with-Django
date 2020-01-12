from django.http import Http404
from django.shortcuts import get_object_or_404
from rest_framework import viewsets, status, filters, authentication, permissions, views
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError
from projects import serializers
from core.permissions import IsAdminOrReadOnly
from core.models import MyProfile
from core.models_project import ProjectModel, ProjectPhaseModel, IssueModel, TeamRequirementsModel, TeamMemberModel, \
    CommitSkillModel, ProjectMessageModel, GamificationAdviceModel


class ProjectModelViewSet(viewsets.ModelViewSet):
    """Project Viewset"""
    authentication_classes = (authentication.TokenAuthentication, authentication.SessionAuthentication)
    permission_classes = (permissions.IsAuthenticated, IsAdminOrReadOnly)  ## DEL ADMIN ONLY, CREATE PM
    serializer_class = serializers.ProjectModelSerializer
    filter_backends = (filters.SearchFilter, filters.OrderingFilter)
    search_fields = ("name", "proposed_by")
    queryset = ProjectModel.objects.all()

    def get_queryset(self):
        """Return list of charities"""
        queryset = self.queryset
        return queryset.order_by('name')

    def perform_create(self, serializer):
        """Start new project"""
        serializer.save(proposed_by=self.request.user)


class TeamRequirementsViewSet(views.APIView):
    """Team Requirements Viewset"""

    def get(self, request):
        return Response({"asd": "zxc"})

