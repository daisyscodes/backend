from django.db import models
from authentication.models import User
from functools import partial


GENRE = (
    ("Unknown", "Unknown"),
    ("Movie", "Movie"),
    ("Rap", "Rap"),
    ("Pop", "Pop"),
    ("Rock", "Rock"),
    ("Alternative/Indie", "Alternative/Indie"),
    ("Remix", "Remix"),
    ("Instrumental", "Instrumental"),
    ("Folk", "Folk"),
    ("Electronic", "Electronic")
)


def make_filepath(field_name, instance, filename):
    new_filename = "%s.%s" % (User.objects.make_random_password(10),
                              filename.split('.')[-1])
    return '/'.join([instance.__class__.__name__.lower(),
                     field_name, new_filename])


class Artist(models.Model):
    nick_name = models.CharField(max_length=200, default='Def')
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    history = models.TextField(blank=True)
    photo = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.first_name + ' ' + self.last_name


class Band(models.Model):
    name = models.CharField(max_length=200)
    cover = models.CharField(max_length=100, null=True)


class Album(models.Model):
    name = models.CharField(max_length=45, null=False)
    genre = models.CharField(max_length=200, choices=GENRE, default=GENRE[0][0])
    cover = models.CharField(max_length=100, null=True)
    single = models.BooleanField(default=False)
    description = models.TextField(null=True, blank=True)
    artists = models.ManyToManyField(Artist, null=True, blank=True, related_name='album_artist')
    band = models.ForeignKey(Band, on_delete=models.DO_NOTHING, null=True, blank=True,
                             default=None, related_name='album_band')

    def __str__(self):
        return self.name


class Music(models.Model):
    name = models.CharField(max_length=45, null=False)
    file = models.CharField(max_length=200)
    albums = models.ForeignKey(Album, on_delete=models.CASCADE, null=True, related_name='music_album')

    def __str__(self):
        return self.name


class Playlist(models.Model):
    name = models.CharField(max_length=45, null=False)
    cover = models.CharField(max_length=100, null=True)
    musics = models.ManyToManyField(Music, null=True)
    private = models.BooleanField(default=False)

    def __str__(self):
        return self.name
