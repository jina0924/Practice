from django.contrib import admin
from .models import Artist, Music


class ArtistAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name',)


class MusicAdmin(admin.ModelAdmin):
    list_display = ('pk', 'artist_id', 'title')


admin.site.register(Artist, ArtistAdmin)
admin.site.register(Music, MusicAdmin)