from django.http import Http404
from django.shortcuts import get_object_or_404
from rest_framework import viewsets, status, filters, authentication, permissions, views, generics
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError
from projects import serializers
from core.permissions import IsAdminOrReadOnly, IsOwnerOrReadOnly, IsFixingOrReadOnly, IsAdminOrReadAndCreateOnly
from core import models
from core import models_project

from projects.utils import project_prize


class ProjectModelViewSet(viewsets.ModelViewSet):
    """Project Viewset"""
    authentication_classes = (authentication.TokenAuthentication, authentication.SessionAuthentication)
    permission_classes = (IsAdminOrReadAndCreateOnly,)
    serializer_class = serializers.ProjectModelSerializer
    filter_backends = (filters.SearchFilter, filters.OrderingFilter)
    search_fields = ("name", "proposed_by")
    queryset = models_project.ProjectModel.objects.all()

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
    permission_classes = (permissions.IsAuthenticated, IsOwnerOrReadOnly)  # DEL ADMIN ONLY, CREATE PM
    serializer_class = serializers.TeamRequirementsModelSerializer

    def get(self, request, pk):
        """Get team requirements for specific project"""
        team_requirements = get_object_or_404(models_project.TeamRequirementsModel, project=pk)
        serializer_context = {"request": request}
        serializer = self.serializer_class(team_requirements, context=serializer_context)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        """Create team requirements for specific project"""
        team_requirements = get_object_or_404(models_project.TeamRequirementsModel, project=pk)
        serializer = serializers.TeamRequirementsModelSerializer(team_requirements, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProjectPhaseViews(views.APIView):
    """View for advancing project"""
    authentication_classes = (authentication.TokenAuthentication, authentication.SessionAuthentication)
    permission_classes = (permissions.IsAuthenticated, IsAdminOrReadOnly)  # DEL ADMIN ONLY, CREATE PM
    serializer_class = serializers.ProjectPhaseSerializer

    def get(self, request, pk):
        """Get project phase specific project"""
        project_phase = get_object_or_404(models_project.ProjectModel, id=pk)
        serializer_context = {"request": request}
        serializer = self.serializer_class(project_phase, context=serializer_context)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def patch(self, request, pk):
        """Advance project to the next phase"""
        project_phase = get_object_or_404(models_project.ProjectModel, id=pk)
        serializer = serializers.ProjectPhaseSerializer(project_phase, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CompleteProjectView(views.APIView):
    """View for completing project"""
    authentication_classes = (authentication.TokenAuthentication, authentication.SessionAuthentication)
    permission_classes = (permissions.IsAuthenticated, IsAdminOrReadOnly)

    def get(self, request, pk):
        return Response({"message": f"Finish the project with id: {pk}"}, status=status.HTTP_200_OK)

    def post(self, request, pk):
        """Finish the project"""
        project = get_object_or_404(models_project.ProjectModel, id=pk)
        project_team = models_project.TeamMembershipModel.objects.filter(project=project)
        project_manager = models.MyProfile.objects.get(owner=project.proposed_by)

        team_members, prize = project_prize(project, project_team)

        project_manager.my_wallet = project_manager.my_wallet + 540
        project_manager.save()

        for element in project_team:
            member = element.member
            winners = models.MyProfile.objects.filter(owner=member)
            for element in winners:
                element.my_wallet += prize
                element.save()

        project.delete()
        return Response(
            ({"message": f"Project was successfully completed. Each of {team_members} team members "
                         f"received {prize} LeanCoins. Additionally 540 LeanCoins has been transferred "
                         f"to {project_manager} for successful project completion"}),
            status=status.HTTP_204_NO_CONTENT)


class TeamJoinView(views.APIView):
    """View for joining project team"""
    authentication_classes = (authentication.TokenAuthentication, authentication.SessionAuthentication)
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = serializers.TeamMembershipModelSerializer

    def post(self, request, pk):
        request_user = self.request.user
        project = get_object_or_404(models_project.ProjectModel, id=pk)
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            profile = get_object_or_404(models.MyProfile, owner=request_user)
            if profile.personality == "":
                return Response({"error": "You have to submit gamification test at your Profile page first."},
                                status=status.HTTP_400_BAD_REQUEST)
            serializer.save(member=request_user, project=project)
            return Response(serializer.data,  status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TeamRejectView(views.APIView):
    """View for rejecting team member"""
    authentication_classes = (authentication.TokenAuthentication, authentication.SessionAuthentication)
    permission_classes = (permissions.IsAuthenticated, IsOwnerOrReadOnly)
    serializer_class = serializers.TeamRejectionSerializer

    def get(self, request, pk, id):
        project = get_object_or_404(models_project.ProjectModel, id=pk)
        team_member = get_object_or_404(models_project.TeamMembershipModel, project=project, member=id)
        serializer_context = {"request": request}
        serializer = self.serializer_class(team_member, context=serializer_context)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def delete(self, request, pk, id):
        project = get_object_or_404(models_project.ProjectModel, id=pk)
        try:
            team_member = get_object_or_404(models_project.TeamMembershipModel, project=project, member=id)
            team_member.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except TeamMembershipModel.DoesNotExist:
            raise Http404


class IssueCreateView(views.APIView):
    """Project Issue Viewset"""
    authentication_classes = (authentication.TokenAuthentication, authentication.SessionAuthentication)
    permission_classes = (permissions.IsAuthenticated, IsOwnerOrReadOnly)
    serializer_class = serializers.IssueCreateSerializer

    def get(self, request, pk):
        return Response({"message": f"Report an issue for the project with id: {pk}"}, status=status.HTTP_200_OK)

    def post(self, request, pk):
        request_user = self.request.user
        project = get_object_or_404(models_project.ProjectModel, id=pk)
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save(assigned_to=request_user, project=project)
            models_project.ProjectMessageModel.objects.create(project=project,
                                                              message=f"Issue '{request.data['name']}' "
                                                                      f"raised by PM {request_user}."
                                                              ).save()

            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class IssueAssignView(views.APIView):
    """Assign Issue Viewset"""
    authentication_classes = (authentication.TokenAuthentication, authentication.SessionAuthentication)
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request, id):
        return Response({"message": f"Assign issue id: {id} to yourself"}, status=status.HTTP_200_OK)

    def patch(self, request, id):
        issue = get_object_or_404(models_project.IssueModel, id=id)
        try:
            issue.assigned_to = self.request.user
            issue.save()
            models_project.ProjectMessageModel.objects.create(
                project=issue.project,
                message='Issue "{0}" assigned to user {1}'.format(issue.name, issue.assigned_to)
            ).save()
            return Response({"message": "Issue was successfully assigned to you"}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error": "We couldn't assign that Issue to you at this time. Try again later"},
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class IssueFixedView(views.APIView):
    """Assign Issue Viewset"""
    authentication_classes = (authentication.TokenAuthentication, authentication.SessionAuthentication)
    permission_classes = (permissions.IsAuthenticated, IsFixingOrReadOnly)

    def get(self, request, id):
        return Response({"message": f"Close issue id: {id}"})

    def post(self, request, id):
        issue = get_object_or_404(models_project.IssueModel, id=id)
        my_profile = get_object_or_404(models.MyProfile, owner=request.user)
        try:
            my_profile.my_wallet = my_profile.my_wallet + issue.cost
            my_profile.save()
            issue.delete()
            models_project.ProjectMessageModel.objects.create(
                project=issue.project,
                message='Issue "{0}" fixed by user {1}'.format(issue.name, issue.assigned_to)).save()
        except Exception as e:
            return Response({"error": "We couldn't proceed with closing the Issue at this time. Try again later"})


class IssueCountView(views.APIView):
    """Issue Counter"""
    authentication_classes = (authentication.TokenAuthentication, authentication.SessionAuthentication)
    permission_classes = (IsAdminOrReadOnly,)

    def get(self, request):
        queryset = models_project.IssueModel.objects.all()
        return Response({"issue_count": len(queryset)})
