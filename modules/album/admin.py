from django.contrib import admin
from modules.album.models import Album


@admin.register(Album)
class AlbumAdmin(admin.ModelAdmin):
    '''Admin View for Album'''

    list_display = ('title', 'duration', 'artist',)
    search_fields = ('title', 'artist',)
    ordering = ('-id',)