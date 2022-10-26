"""
Tests for the artist API.
"""
from django.contrib.auth import get_user_model
from django.urls import reverse
from django.test import TestCase

from rest_framework import status
from rest_framework.test import APIClient

from modules.artist.models import Artist

from modules.artist.serializers import ArtistSerializer, ArtistDetailSerializer


ARTIST_URL = reverse('artist:artist-list')


def detail_url(artist_id):
    """Create and return an artist detail URL."""
    return reverse('artist:artist-detail', args=[artist_id])


def create_user(email='user@example.com', password='testpass123', full_name="full name", username="user name"):
    """Create and return user."""
    return get_user_model().objects.create_user(email=email, password=password, full_name=full_name, username=username)


class PublicArtistsApiTests(TestCase):
    """Test unauthenticated API requests."""

    def setUp(self):
        self.client = APIClient()

    def test_auth_required(self):
        """Test auth is required for retrieving artists."""
        res = self.client.get(ARTIST_URL)

        self.assertEqual(res.status_code, status.HTTP_401_UNAUTHORIZED)


class PrivateArtistsApiTests(TestCase):
    """Test authenticated API requests."""

    def setUp(self):
        self.user = create_user()
        self.client = APIClient()
        self.client.force_authenticate(self.user)

    def test_retrieve_artist(self):
        """Test retrieving a list of artist."""
        Artist.objects.create(full_name='alejandro sosa', sumary='big voice')
        Artist.objects.create(full_name='slikpnot', sumary='excelent')

        res = self.client.get(ARTIST_URL)

        artist = Artist.objects.all().order_by('-id')
        serializer = ArtistDetailSerializer(artist, many=True)
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data, serializer.data)

    def test_update_artist(self):
        """Test updating an artist."""
        artist = Artist.objects.create(full_name='alejandro sosa', sumary='big voice')

        payload = {'full_name': 'Coriander'}
        url = detail_url(artist.id)
        res = self.client.patch(url, payload)

        self.assertEqual(res.status_code, status.HTTP_200_OK)
        artist.refresh_from_db()
        self.assertEqual(artist.full_name, payload['full_name'])

    def test_delete_artist(self):
        """Test deleting an artist."""
        artist = Artist.objects.create(full_name='alejandro sosa', sumary='big voice')

        url = detail_url(artist.id)
        res = self.client.delete(url)

        self.assertEqual(res.status_code, status.HTTP_204_NO_CONTENT)
        artists = Artist.objects.filter()
        self.assertFalse(artists.exists())

    def test_create_artist(self):
        """Test creating a artist."""
        payload = {
            'full_name': 'slikpnot',
            'sumary': 'excelent'
        }
        res = self.client.post(ARTIST_URL, payload, format='json')

        self.assertEqual(res.status_code, status.HTTP_201_CREATED)
        artists = Artist.objects.filter()
        self.assertEqual(artists.count(), 1)