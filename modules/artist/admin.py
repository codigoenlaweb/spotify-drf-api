from django.contrib import admin
from modules.artist.models import Artist


@admin.register(Artist)
class ArtistAdmin(admin.ModelAdmin):
    '''Admin View for Artist'''

    list_display = ('full_name', 'sumary',)
    search_fields = ('full_name',)
    ordering = ('-id',)
