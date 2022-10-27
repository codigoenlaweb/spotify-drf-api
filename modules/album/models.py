from datetime import timedelta
from django.db import models
from django.utils.translation import gettext_lazy as _
from modules.artist.models import Artist


class Album(models.Model):
    """Object Album."""

    title = models.CharField(_('title'), max_length=250)
    duration = models.IntegerField(
        _("duration"), blank=True, default=0, help_text=_("works in seconds"))  # seconds
    artist = models.ForeignKey(
        Artist, verbose_name=_("artist"),
        on_delete=models.CASCADE,
        related_name='albums',
        related_query_name='album'
    )

    class Meta:
        """Meta definition for Album."""

        verbose_name = 'Album'
        verbose_name_plural = 'Albums'

    def __str__(self):
        """Unicode representation of Album."""
        return f'{self.title}'

    # def save(self):
    #     """Save method for Album."""
    #     pass
