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


class TeamRequirementsViews(views.APIView):
    """Team Requirements Views"""
    authentication_classes = (authentication.TokenAuthentication, authentication.SessionAuthentication)
    permission_classes = (permissions.IsAuthenticated, IsAdminOrReadOnly)  ## DEL ADMIN ONLY, CREATE PM
    serializer_class = serializers.TeamRequirementsModelSerializer

    def get(self, request, pk):
        """Get team requirements for specific project"""
        team_requirements = get_object_or_404(TeamRequirementsModel, project=pk)
        serializer_context = {"request": request}
        serializer = self.serializer_class(team_requirements, context=serializer_context)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        """Create team requirements for specific project"""
        team_requirements = get_object_or_404(TeamRequirementsModel, project=pk)
        serializer = serializers.TeamRequirementsModelSerializer(team_requirements, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


