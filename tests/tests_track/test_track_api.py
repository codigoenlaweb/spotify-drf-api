"""
Tests for the artist API.
"""
from datetime import timedelta
from django.contrib.auth import get_user_model
from django.urls import reverse
from django.test import TestCase

from rest_framework import status
from rest_framework.test import APIClient

from modules.track.models import Track
from modules.album.models import Album
from modules.artist.models import Artist

from modules.track.serializers import TrackSerializer, TrackDetailSerializer


TRACK_URL = reverse('track:track-list')


def detail_url(track_id):
    """Create and return an track detail URL."""
    return reverse('track:track-detail', args=[track_id])


def create_user(email='user@example.com', password='testpass123', full_name="full name", username="user name"):
    """Create and return user."""
    return get_user_model().objects.create_user(email=email, password=password, full_name=full_name, username=username)


class PublicTracksApiTests(TestCase):
    """Test unauthenticated API requests."""

    def setUp(self):
        self.client = APIClient()

    def test_auth_required(self):
        """Test auth is required for retrieving artists."""
        res = self.client.get(TRACK_URL)

        self.assertEqual(res.status_code, status.HTTP_401_UNAUTHORIZED)


class PrivateTracksApiTests(TestCase):
    """Test authenticated API requests."""

    def setUp(self):
        self.user = create_user()
        self.client = APIClient()
        self.client.force_authenticate(self.user)

    def test_retrieve_track(self):
        """Test retrieving a list of track."""

        artist = Artist.objects.create(
            full_name='alejandro sosa', sumary='big voice')
        album = Album.objects.create(title="anithyn title", artist=artist)
        Track.objects.create(title='titulo1', duration=200,
                             album=album, url_track='https://youtube.com')
        Track.objects.create(title='titulo2', duration=200,
                             album=album, url_track='https://youtube.com')

        res = self.client.get(TRACK_URL)

        track = Track.objects.all().order_by('-id')
        serializer = TrackDetailSerializer(track, many=True)
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data, serializer.data)

    def test_update_track(self):
        """Test updating an album."""

        artist = Artist.objects.create(
            full_name='alejandro sosa', sumary='big voice')
        album = Album.objects.create(title="anithyn title", artist=artist)
        track = Track.objects.create(
            title='titulo1', duration=200, album=album, url_track='https://youtube.com')

        payload = {'title': 'change title'}
        url = detail_url(track.id)
        res = self.client.patch(url, payload)

        self.assertEqual(res.status_code, status.HTTP_200_OK)
        track.refresh_from_db()
        self.assertEqual(track.title, payload['title'])

    def test_delete_track(self):
        """Test deleting an track."""
        artist = Artist.objects.create(
            full_name='alejandro sosa', sumary='big voice')
        album = Album.objects.create(title="anithyn title", artist=artist)
        track = Track.objects.create(
            title='titulo1', duration=200, album=album, url_track='https://youtube.com')

        url = detail_url(track.id)
        res = self.client.delete(url)

        self.assertEqual(res.status_code, status.HTTP_204_NO_CONTENT)
        track = Track.objects.filter()
        self.assertFalse(track.exists())

    def test_create_track(self):
        """Test creating a track."""
        artist = Artist.objects.create(
            full_name='alejandro sosa', sumary='big voice')
        album = Album.objects.create(title="anithyn title", artist=artist)
        payload = {
            "title": "title new",
            "duration": "200",
            "album": album.id,
            "url_track": 'https://youtube.com'
        }
        res = self.client.post(TRACK_URL, payload, format='json')

        self.assertEqual(res.status_code, status.HTTP_201_CREATED)
        track = Track.objects.filter()
        self.assertEqual(track.count(), 1)

