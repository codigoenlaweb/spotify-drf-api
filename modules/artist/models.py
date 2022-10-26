from django.db import models
from django.utils.translation import gettext_lazy as _


class Artist(models.Model):
    """Object Artist."""

    full_name = models.CharField(_('full name'), max_length=250)
    sumary = models.TextField(_("sumary"), blank=True, null=True)

    class Meta:
        """Meta definition for Artist."""

        verbose_name = 'Artist'
        verbose_name_plural = 'Artists'

    def __str__(self):
        """Unicode representation of Artist."""
        return f'{self.full_name}'

    # def save(self):
    #     """Save method for Artist."""
    #     pass
