from datetime import timedelta
from django.db import models
from django.utils.translation import gettext_lazy as _
from modules.album.models import Album


class Track(models.Model):
    """Object Album."""

    title = models.CharField(_('title'), max_length=250)
    duration = models.IntegerField(_("duration"), blank=True, default=0, help_text=_("works in seconds")) # seconds
    url_track = models.URLField(_("url track"), max_length=250,)
    album = models.ForeignKey(
        Album, verbose_name=_("artist"),
        on_delete=models.CASCADE,
        related_name='tracks',
        related_query_name='track'
    )

    class Meta:
        """Meta definition for Track."""

        verbose_name = 'Track'
        verbose_name_plural = 'Tracks'

    def __str__(self):
        """Unicode representation of Track."""
        return self.title

    def save(self, *args, **kwargs):
        super(Track, self).save(*args, **kwargs)
        tracks = Track.objects.filter(album=self.album)
        secons_all = 0
        for track in tracks:
            secons_all += track.duration
        self.album.duration = secons_all
        self.album.save()


