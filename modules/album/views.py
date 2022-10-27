"""
Views for the album APIs
"""
from django.shortcuts import get_object_or_404
from rest_framework import (
    viewsets,
    mixins,
)
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from .models import Album
from .serializers import AlbumSerializer, AlbumDetailSerializer
from rest_framework.response import Response


class AlbumViewSet(viewsets.ModelViewSet):
    """Manage Albums in the database."""
    serializer_class = AlbumSerializer
    queryset = Album.objects.all()
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        """Filter queryset if user is authenticated."""
        return self.queryset.filter().order_by('-id')

    def list(self, request):
        queryset = self.queryset.filter().order_by('-id')
        serializer = AlbumDetailSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = self.queryset.filter().order_by('-id')
        album = get_object_or_404(queryset, pk=pk)
        serializer = AlbumDetailSerializer(album)
        return Response(serializer.data)