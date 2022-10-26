"""
Views for the user API.
"""
from datetime import datetime
from django.contrib.sessions.models import Session
from rest_framework import status
from rest_framework.response import Response
from rest_framework import generics, authentication, permissions, views
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings
from modules.users.serializers import (
    UserSerializer,
    AuthTokenSerializer,
)
from drf_spectacular.utils import extend_schema

class CreateUserView(generics.CreateAPIView):
    """Create a new user in the system."""
    serializer_class = UserSerializer



class CreateTokenView(ObtainAuthToken):
    """
    Login and create a new auth token for user.
    """
    serializer_class = AuthTokenSerializer
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES


class LogoutUserView(views.APIView):
    """Manage the authenticated user."""
    serializer_class = AuthTokenSerializer
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, *args, **kwargs):
        request.user.auth_token.delete()
        request.session.delete
        return Response(status=status.HTTP_200_OK)



class ManageUserView(generics.RetrieveUpdateAPIView):
    """Manage the authenticated user."""
    serializer_class = UserSerializer
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        """Retrieve and return the authenticated user."""
        return self.request.user