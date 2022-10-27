"""
Serializers for Track APIs
"""
from rest_framework import serializers
from .models import Track
from modules.album.models import Album
from modules.artist.models import Artist


class ArtistForTrackSerializer(serializers.ModelSerializer):
    """Serializer for Track from Artist."""

    class Meta:
        model = Artist
        fields = ['id', 'full_name', 'sumary']
        read_only_fields = ['id']


class AlbumForTrackSerializer(serializers.ModelSerializer):
    """Serializer for Track from Album."""
    artist = ArtistForTrackSerializer()

    class Meta:
        model = Album
        fields = ['id', 'title', 'duration', 'artist']
        read_only_fields = ['id', 'duration', 'artist']


class TrackSerializer(serializers.ModelSerializer):
    """Serializer for Track."""

    class Meta:
        model = Track
        fields = ['id', 'title', 'duration', 'url_track', 'album']
        read_only_fields = ['id']


class TrackDetailSerializer(serializers.ModelSerializer):
    """Serializer for Track."""
    album = AlbumForTrackSerializer()

    class Meta:
        model = Track
        fields = ['id', 'title', 'duration', 'url_track', 'album']
        read_only_fields = ['id', 'album']
