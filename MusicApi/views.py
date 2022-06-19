from django.shortcuts import render
from rest_framework import viewsets, generics
from . import serializers
from . import models
from random import randint


class PlaylistViewSet(viewsets.ModelViewSet):
    queryset = models.Playlist.objects.all()
    serializer_class = serializers.PlaylistSerializer


class AlbumViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.AlbumSerializer

    def get_queryset(self):
        queryset = models.Album.objects.all()
        count = self.request.query_params.get('count')
        if count:
            q_from = self.ran(len(queryset) - int(count))
            if q_from<0:
                q_from=0
            queryset = queryset[q_from: q_from + int(count)]

        return queryset

    def ran(self, num):
        return randint(0, num)


class BandViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.BandSerializer

    def get_queryset(self):
        queryset = models.Band.objects.all()
        count = self.request.query_params.get('count')
        if count:
            q_from = self.ran(len(queryset) - int(count))
            if q_from<0:
                q_from=0
            queryset = queryset[q_from: q_from + int(count)]

        return queryset

    def ran(self, num):
        return randint(0, num)


class MusicViewSet(viewsets.ModelViewSet):
    queryset = models.Music.objects.all()
    serializer_class = serializers.MusicSerializer


class ArtistViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.ArtistSerializer

    def get_queryset(self):
        queryset = models.Artist.objects.all()
        count = self.request.query_params.get('count')
        if count:
            q_from = self.ran(len(queryset) - int(count))
            if q_from < 0:
                q_from = 0
            queryset = queryset[q_from: q_from + int(count)]

        return queryset

    def ran(self, num):
        return randint(0, num)
