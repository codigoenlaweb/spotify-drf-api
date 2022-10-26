"""
Serializers for artist APIs
"""
from rest_framework import serializers
from .models import Artist
from modules.album.models import Album


class AlbumForArtistSerializer(serializers.ModelSerializer):
    """Serializer for Artists."""

    class Meta:
        model = Album
        fields = ['id', 'title', 'duration', 'artist']
        read_only_fields = ['id', 'duration']


class ArtistSerializer(serializers.ModelSerializer):
    """Serializer for Artists."""

    class Meta:
        model = Artist
        fields = ['id', 'full_name', 'sumary']
        read_only_fields = ['id']


class ArtistDetailSerializer(serializers.ModelSerializer):
    """Serializer for Artists."""
    albums = AlbumForArtistSerializer(many=True)

    class Meta:
        model = Artist
        fields = ['id', 'full_name', 'sumary', 'albums']
        read_only_fields = ['id']
