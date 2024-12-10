
from rest_framework import serializers
from .models import User, Artists, Events, EventsxArtist, Merch, ArtistsXSongs, Songs, Playlists, SongsXlists, Tags, TagsxSongs

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id','username','email','phone_number','password']
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
        fields = ['__all__']

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Events
        fields = ['__all__']

class EventxArtistSerializer(serializers.ModelSerializer):
    class Meta:
        model = EventsxArtist
        fields = ['__all__']

class MerchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Merch
        fields = ['__all__']

class ArtistxSongSerializer(serializers.ModelSerializer):
    class Meta:
        model = ArtistsXSongs
        fields = ['__all__']

class SongSerializer(serializers.ModelSerializer):
    class Meta:
        model = Songs
        fields = ['__all__']

class PlaylistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Playlists
        fields = ['__all__']

class SongxListSerializer(serializers.ModelSerializer):
    class Meta:
        model = SongsXlists
        fields = ['__all__']

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tags
        fields = ['__all__']

class TagxSongSerializer(serializers.ModelSerializer):
    class Meta:
        model = TagsxSongs
        fields = ['__all__']
