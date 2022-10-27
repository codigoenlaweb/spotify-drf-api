"""
Views for the album APIs
"""
from django.shortcuts import get_object_or_404
from rest_framework import (
    viewsets,
    mixins,
    generics
)
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from .models import Track
from .serializers import TrackSerializer, TrackDetailSerializer
from rest_framework.response import Response
from drf_spectacular.utils import extend_schema, OpenApiParameter, OpenApiExample
from drf_spectacular.types import OpenApiTypes
from rest_framework import filters

class TrackViewSet(viewsets.ModelViewSet):
    """Manage Tracks in the database."""
    serializer_class = TrackSerializer
    queryset = Track.objects.all()
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        """Filter queryset if user is authenticated."""
        return self.queryset.filter().order_by('-id')

    def list(self, request):
        queryset = self.queryset.filter().order_by('-id')
        serializer = TrackDetailSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = self.queryset.filter().order_by('-id')
        album = get_object_or_404(queryset, pk=pk)
        serializer = TrackDetailSerializer(album)
        return Response(serializer.data)

@extend_schema(
    # extra parameters added to the schema
    parameters=[
        OpenApiParameter(
            name='search',
            description='search title from track and title from album',
            examples=[
                OpenApiExample(
                    'Example 1',
                    value='hombre g'
                ),
            ],
        ),
    ],
    # override default docstring extraction
    description='More descriptive text',
)
class SearchTrackView(generics.ListCreateAPIView):
    """Manage Tracks in the database."""
    serializer_class = TrackDetailSerializer
    queryset = Track.objects.all()
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    filter_backends = [filters.SearchFilter]
    search_fields = ['title', 'album__title']