from django.urls import path,include 
from rest_framework import routers
from . import views
router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet, basename='user')
router.register(r'artists', views.ArtistViewSet, basename='artist')

router.register(r'events', views.EventViewSet, basename='event')
router.register(r'eventsxartists',views.EventxArtistViewSet, basename='eventxartist')
router.register(r'merchs', views.MerchViewSet, basename='merch')
router.register(r'artistsxsongs', views.ArtistxSongViewSet, basename='artistxsong')
router.register(r'songs', views.SongViewSet, basename='song')
router.register(r'playlists', views.PlaylistViewSet, basename='playlist')
router.register(r'songsxlists', views.SongxListViewSet, basename='songxlist')
router.register(r'tags', views.TagViewSet, basename='tag')
router.register(r'tagsxsongs', views.TagxSongViewSet, basename='tagxsong')

urlpatterns = [
    path('',include(router.urls))
]