from django.contrib import admin
from .models import Music, Album, Artist, Playlist
# Register your models here.

admin.site.register(Music)
admin.site.register(Playlist)
admin.site.register(Artist)
admin.site.register(Album)
