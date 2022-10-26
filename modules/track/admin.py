from django.contrib import admin
from modules.track.models import Track


@admin.register(Track)
class TrackAdmin(admin.ModelAdmin):
    '''Admin View for Track'''

    list_display = ('title', 'duration', 'url_track', 'album',)
    search_fields = ('title',)
    ordering = ('-id',)
