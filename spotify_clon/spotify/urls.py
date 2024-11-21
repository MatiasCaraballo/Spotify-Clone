from rest_framework import viewsets, routers
from .models import User, Artists, Events, EventsxArtist, Merch, ArtistsXSongs, Songs, Playlists, SongsXlists, Tags, TagsxSongs
from .serializers import UserSerializer, ArtistSerializer, EventSerializer, EventxArtistSerializer, MerchSerializer, ArtistxSongSerializer, SongSerializer, PlaylistSerializer, SongxListSerializer, TagSerializer, TagxSongSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class ArtistViewSet(viewsets.ModelViewSet):
    queryset = Artists.objects.all()
    serializer_class = ArtistSerializer

class EventViewSet(viewsets.ModelViewSet):
    queryset = Events.objects.all()
    serializer_class = EventSerializer

class EventxArtistViewSet(viewsets.ModelViewSet):
    queryset = EventsxArtist.objects.all()
    serializer_class = EventxArtistSerializer

class MerchViewSet(viewsets.ModelViewSet):
    queryset = Merch.objects.all()
    serializer_class = MerchSerializer

class ArtistxSongViewSet(viewsets.ModelViewSet):
    queryset = ArtistsXSongs.objects.all()
    serializer_class = ArtistxSongSerializer

class SongViewSet(viewsets.ModelViewSet):
    queryset = Songs.objects.all()
    serializer_class = SongSerializer

class PlaylistViewSet(viewsets.ModelViewSet):
    queryset = Playlists.objects.all()
    serializer_class = PlaylistSerializer

class SongxListViewSet(viewsets.ModelViewSet):
    queryset = SongsXlists.objects.all()
    serializer_class = SongxListSerializer

class TagViewSet(viewsets.ModelViewSet):
    queryset = Tags.objects.all()
    serializer_class = TagSerializer

class TagxSongViewSet(viewsets.ModelViewSet):
    queryset = TagsxSongs.objects.all()
    serializer_class = TagxSongSerializer

router = routers.DefaultRouter()
router.register('users', UserViewSet, basename='user')
router.register('artists', ArtistViewSet, basename='artist')
router.register('events', EventViewSet, basename='event')
router.register('eventsxartists', EventxArtistViewSet, basename='eventxartist')
router.register('merchs', MerchViewSet, basename='merch')
router.register('artistsxsongs', ArtistxSongViewSet, basename='artistxsong')
router.register('songs', SongViewSet, basename='song')
router.register('playlists', PlaylistViewSet, basename='playlist')
router.register('songsxlists', SongxListViewSet, basename='songxlist')
router.register('tags', TagViewSet, basename='tag')
router.register('tagsxsongs', TagxSongViewSet, basename='tagxsong')

urlpatterns = router.urls
