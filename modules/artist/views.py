"""
Views for the artist APIs
"""
from django.shortcuts import get_object_or_404
from rest_framework import (
    viewsets,
    mixins,
)
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from .models import Artist
from .serializers import ArtistSerializer, ArtistDetailSerializer
from rest_framework.response import Response

class ArtistViewSet(viewsets.ModelViewSet):
    """Manage artists in the database."""
    serializer_class = ArtistSerializer
    queryset = Artist.objects.all()
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        """Filter queryset if user is authenticated."""
        return self.queryset.filter().order_by('-id')

    def list(self, request):
        queryset = self.queryset.filter().order_by('-id')
        serializer = ArtistDetailSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = self.queryset.filter().order_by('-id')
        artist = get_object_or_404(queryset, pk=pk)
        serializer = ArtistDetailSerializer(artist)
        return Response(serializer.data)