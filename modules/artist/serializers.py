"""
Serializers for artist APIs
"""
from rest_framework import serializers
from .models import Artist
from modules.album.models import Album
from modules.track.models import Track


class TracksForArtistSerializer(serializers.ModelSerializer):
    """Serializer for Artists from Track."""

    class Meta:
        model = Track
        fields = ['id', 'title', 'duration', 'album']
        read_only_fields = ['id']


class AlbumsForArtistSerializer(serializers.ModelSerializer):
    """Serializer for Artists from Album."""
    tracks = TracksForArtistSerializer(many=True)

    class Meta:
        model = Album
        fields = ['id', 'title', 'duration', 'tracks']
        read_only_fields = ['id', 'duration', 'tracks']


class ArtistSerializer(serializers.ModelSerializer):
    """Serializer for Artists."""

    class Meta:
        model = Artist
        fields = ['id', 'full_name', 'sumary']
        read_only_fields = ['id']


class ArtistDetailSerializer(serializers.ModelSerializer):
    """Serializer for Artists."""
    albums = AlbumsForArtistSerializer(many=True)

    class Meta:
        model = Artist
        fields = ['id', 'full_name', 'sumary', 'albums']
        read_only_fields = ['id']
