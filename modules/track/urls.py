"""
URL mappings for the track app.
"""
from django.urls import (
    path,
    include,
)
from rest_framework.routers import DefaultRouter
from . import views
router = DefaultRouter()
router.register('', views.TrackViewSet)

app_name = 'track'

urlpatterns = [
    path('', include(router.urls)),
    path('search', views.SearchTrackView.as_view()),
]