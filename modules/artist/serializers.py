"""
Serializers for Artist APIs
"""
from rest_framework import serializers
from .models import Artist


class ArtistSerializer(serializers.ModelSerializer):
    """Serializer for Artists."""

    class Meta:
        model = Artist
        fields = ['full_name', 'sumary']
        read_only_fields = ['id']