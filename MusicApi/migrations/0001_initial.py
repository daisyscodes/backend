# Generated by Django 2.2.13 on 2021-05-16 17:24

import MusicApi.models
from django.db import migrations, models
import django.db.models.deletion
import functools


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=45)),
                ('genre', models.CharField(choices=[('Unknown', 'Unknown'), ('Movie', 'Movie'), ('Rap', 'Rap'), ('Pop', 'Pop'), ('Rock', 'Rock'), ('Alternative/Indie', 'Alternative/Indie'), ('Remix', 'Remix'), ('Instrumental', 'Instrumental'), ('Folk', 'Folk'), ('Electronic', 'Electronic')], default='Unknown', max_length=200)),
                ('cover', models.ImageField(upload_to=functools.partial(MusicApi.models.make_filepath, *('album_covers/',), **{}))),
                ('single', models.BooleanField(default=False)),
                ('description', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Artist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nick_name', models.CharField(default='Def', max_length=200)),
                ('first_name', models.CharField(max_length=200)),
                ('last_name', models.CharField(max_length=200)),
                ('history', models.TextField(blank=True)),
                ('photo', models.ImageField(blank=True, upload_to=functools.partial(MusicApi.models.make_filepath, *('artist_photo/',), **{}))),
            ],
        ),
        migrations.CreateModel(
            name='Band',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('cover', models.ImageField(upload_to=functools.partial(MusicApi.models.make_filepath, *('band_covers/',), **{}))),
            ],
        ),
        migrations.CreateModel(
            name='Music',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=45)),
                ('file', models.CharField(max_length=200)),
                ('albums', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='music_album', to='MusicApi.Album')),
            ],
        ),
        migrations.CreateModel(
            name='Playlist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=45)),
                ('cover', models.ImageField(upload_to=functools.partial(MusicApi.models.make_filepath, *('pl_covers/',), **{}))),
                ('private', models.BooleanField(default=False)),
                ('musics', models.ManyToManyField(null=True, to='MusicApi.Music')),
            ],
        ),
        migrations.AddField(
            model_name='album',
            name='artists',
            field=models.ManyToManyField(blank=True, null=True, related_name='album_artist', to='MusicApi.Artist'),
        ),
        migrations.AddField(
            model_name='album',
            name='band',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='album_band', to='MusicApi.Band'),
        ),
    ]
