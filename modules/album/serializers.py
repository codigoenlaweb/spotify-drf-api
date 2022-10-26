"""
Serializers for albumAPIs
"""
from rest_framework import serializers
from .models import Album
from modules.artist.serializers import ArtistSerializer


class AlbumSerializer(serializers.ModelSerializer):
    """Serializer for Artists."""

    class Meta:
        model = Album
        fields = ['id', 'title', 'duration', 'artist']
        read_only_fields = ['id', 'duration']


class AlbumDetailSerializer(serializers.ModelSerializer):
    """Serializer for Artists."""
    artist = ArtistSerializer()

    class Meta:
        model = Album
        fields = ['id', 'title', 'duration', 'artist']
        read_only_fields = ['id', 'duration']