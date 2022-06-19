from rest_framework import serializers
from . import models


class MusicSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Music
        fields = ('id','name', 'albums', 'file')


class AlbumSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Album
        fields = ('id', 'name', 'artists', 'band', 'genre', 'cover', 'single', 'description', 'music_album')


class ArtistSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Artist
        fields = ('id', 'nick_name', 'photo', 'first_name', 'last_name', 'history', 'album_artist')


class PlaylistSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Playlist
        fields = ('id', 'name', 'cover', 'musics')


class BandSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Band
        fields = ('id', 'name', 'cover', 'album_band')
