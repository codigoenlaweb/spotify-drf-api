from datetime import timedelta
from django.db import models
from django.utils.translation import gettext_lazy as _
from modules.album.models import Album


class Track(models.Model):
    """Object Album."""

    title = models.CharField(_('title'), max_length=250)
    duration = models.DurationField(_("duration"), blank=True, default=timedelta(seconds=0))
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
        pass

    # def save(self):
    #     """Save method for Track."""
    #     pass
