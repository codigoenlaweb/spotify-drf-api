"""
Tests for the artist API.
"""
from django.contrib.auth import get_user_model
from django.urls import reverse
from django.test import TestCase

from rest_framework import status
from rest_framework.test import APIClient

from modules.album.models import Album
from modules.artist.models import Artist

from modules.album.serializers import AlbumSerializer, AlbumDetailSerializer


ALBUM_URL = reverse('album:album-list')


def detail_url(album_id):
    """Create and return an album detail URL."""
    return reverse('album:album-detail', args=[album_id])


def create_user(email='user@example.com', password='testpass123', full_name="full name", username="user name"):
    """Create and return user."""
    return get_user_model().objects.create_user(email=email, password=password, full_name=full_name, username=username)


class PublicAlbumsApiTests(TestCase):
    """Test unauthenticated API requests."""

    def setUp(self):
        self.client = APIClient()

    def test_auth_required(self):
        """Test auth is required for retrieving artists."""
        res = self.client.get(ALBUM_URL)

        self.assertEqual(res.status_code, status.HTTP_401_UNAUTHORIZED)


class PrivateAlbumsApiTests(TestCase):
    """Test authenticated API requests."""

    def setUp(self):
        self.user = create_user()
        self.client = APIClient()
        self.client.force_authenticate(self.user)

    def test_retrieve_album(self):
        """Test retrieving a list of album."""

        artist = Artist.objects.create(full_name='alejandro sosa', sumary='big voice');
        Album.objects.create(title="anithyn title", artist=artist)
        Album.objects.create(title="anithyn title 2", artist=artist)

        res = self.client.get(ALBUM_URL)

        album = Album.objects.all().order_by('-id')
        serializer = AlbumDetailSerializer(album, many=True)
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data, serializer.data)

    def test_update_album(self):
        """Test updating an album."""
        artist = Artist.objects.create(full_name='alejandro sosa', sumary='big voice');
        album = Album.objects.create(title="anithyn title", artist=artist)

        payload = {'title': 'change title'}
        url = detail_url(album.id)
        res = self.client.patch(url, payload)

        self.assertEqual(res.status_code, status.HTTP_200_OK)
        album.refresh_from_db()
        self.assertEqual(album.title, payload['title'])

    def test_delete_album(self):
        """Test deleting an album."""
        artist = Artist.objects.create(full_name='alejandro sosa', sumary='big voice');
        album = Album.objects.create(title="anithyn title", artist=artist)

        url = detail_url(album.id)
        res = self.client.delete(url)

        self.assertEqual(res.status_code, status.HTTP_204_NO_CONTENT)
        album = Album.objects.filter()
        self.assertFalse(album.exists())

    def test_create_album(self):
        """Test creating a album."""
        artist = Artist.objects.create(full_name='alejandro sosa', sumary='big voice');
        payload = {'title': 'change title', 'artist': artist.id}
        res = self.client.post(ALBUM_URL, payload, format='json')

        self.assertEqual(res.status_code, status.HTTP_201_CREATED)
        album = Album.objects.filter()
        self.assertEqual(album.count(), 1)