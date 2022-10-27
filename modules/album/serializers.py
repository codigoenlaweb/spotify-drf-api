"""
Serializers for albumAPIs
"""
from rest_framework import serializers
from .models import Album
from modules.artist.models import Artist
from modules.track.models import Track


class ArtistForAlbumSerializer(serializers.ModelSerializer):
    """Serializer for Album from Artist."""

    class Meta:
        model = Artist
        fields = ['id', 'full_name', 'sumary']
        read_only_fields = ['id']


class TracksForAlbumSerializer(serializers.ModelSerializer):
    """Serializer for Album from Tracks."""

    class Meta:
        model = Track
        fields = ['id', 'title', 'duration', 'url_track']



class AlbumSerializer(serializers.ModelSerializer):
    """Serializer for Almbun."""

    class Meta:
        model = Album
        fields = ['id', 'title', 'duration', 'artist']
        read_only_fields = ['id', 'duration']


class AlbumDetailSerializer(serializers.ModelSerializer):
    """Serializer for Album."""
    artist = ArtistForAlbumSerializer()
    tracks = TracksForAlbumSerializer(many=True)

    class Meta:
        model = Album
        fields = ['id', 'title', 'duration', 'artist', 'tracks']
        read_only_fields = ['id', 'duration', 'artist', 'tracks']
