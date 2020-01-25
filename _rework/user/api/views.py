from rest_framework import generics, authentication, permissions, views
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.response import Response
from rest_framework.settings import api_settings
from user.api.serializers import UserSerializer, AuthTokenSerializer

from user.api.serializers import UserSerializer, MyProfileSerializer
from core.models import MyProfile


class CreateUserView(generics.CreateAPIView):
    """Create a new user in the system"""
    permission_classes = (permissions.AllowAny,)
    serializer_class = UserSerializer  # generic view - specify serializer you want to use only


class CreateTokenView(ObtainAuthToken):
    """Create a new auth token for user"""
    serializer_class = AuthTokenSerializer
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES


class ManageUserView(generics.RetrieveUpdateAPIView):
    """Manage the authenticated user"""
    serializer_class = UserSerializer
    authentication_classes = (authentication.TokenAuthentication, authentication.SessionAuthentication)
    permission_classes = (permissions.IsAuthenticated,)

    def get_object(self):
        """Retrieve and return authenticated user"""
        return self.request.user


class CurrentUserApiView(views.APIView):
    """Get currently logged user"""
    authentication_classes = (authentication.TokenAuthentication, authentication.SessionAuthentication)
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request):
        serializer = UserSerializer(request.user)
        return Response(serializer.data)


class CurrentPositionApiVIew(views.APIView):
    """Get currently logged user's position"""
    authentication_classes = (authentication.TokenAuthentication, authentication.SessionAuthentication)
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = MyProfileSerializer

    def get(self, request):
        profile = MyProfile.objects.filter(owner=request.user).first()
        return Response({"position": profile.position})
