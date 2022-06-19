from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PlaylistViewSet, AlbumViewSet, ArtistViewSet, MusicViewSet, BandViewSet


router = DefaultRouter()
router.register('playlists', PlaylistViewSet, 'playlists')
router.register('artists', ArtistViewSet, 'artists')
router.register('musics', MusicViewSet, 'musics')
router.register('albums', AlbumViewSet, 'albums')
router.register('bands', BandViewSet, 'bands')

urlpatterns = [
    path('', include(router.urls)),
]