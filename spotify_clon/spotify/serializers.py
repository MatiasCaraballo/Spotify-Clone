
from rest_framework import serializers
from .models import User, Artists, Events, EventsxArtist, Merch, ArtistsXSongs, Songs, Playlists, SongsXlists, Tags, TagsxSongs

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'phone_number', 'password']
        def create(self, validated_data): 
            user = User(**validated_data) 
            user.set_password(validated_data['password']) 
            user.save() 
            return user
        def update(self, instance, validated_data): 
            if 'password' in validated_data: 
                instance.set_password(validated_data['password'])
                return super().update(instance, validated_data)

class ArtistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artists
        fields = ['id', 'name']

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Events
        fields = ['id', 'name', 'place', 'start_time']

class EventxArtistSerializer(serializers.ModelSerializer):
    class Meta:
        model = EventsxArtist
        fields = ['id', 'id_event', 'id_artist']

class MerchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Merch
        fields = ['id', 'name', 'price', 'id_artist']

class ArtistxSongSerializer(serializers.ModelSerializer):
    class Meta:
        model = ArtistsXSongs
        fields = ['id', 'id_artist','id_song']

class SongSerializer(serializers.ModelSerializer):
    class Meta:
        model = Songs
        fields = ['id', 'name', 'file']

class PlaylistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Playlists
        fields = ['id', 'name', 'description', 'id_user']

class SongxListSerializer(serializers.ModelSerializer):
    class Meta:
        model = SongsXlists
        fields = ['id', 'id_song', 'id_playlist']

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tags
        fields = ['id', 'content']

class TagxSongSerializer(serializers.ModelSerializer):
    class Meta:
        model = TagsxSongs
        fields = ['id', 'id_song', 'id_tag']
