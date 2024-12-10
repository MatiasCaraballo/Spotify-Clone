#

# Create your views here.
from rest_framework import viewsets
from .models import User, Artists, Events, EventsxArtist, Merch, ArtistsXSongs, Songs, Playlists, SongsXlists, Tags, TagsxSongs
from .serializers import UserSerializer, ArtistSerializer, EventSerializer, EventxArtistSerializer, MerchSerializer, ArtistxSongSerializer, SongSerializer, PlaylistSerializer, SongxListSerializer, TagSerializer, TagxSongSerializer
from django.shortcuts import render

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

#WORK WITH TEMPLATES
def home(request):
    return render(request,'index.html')

'''


class index():
    def return_index(self):
        return render('index.html')

# Vistas para User

class UserList(View):
    def get(self, request):
        users = list(User.objects.values())
        return JsonResponse(users, safe=False)

    def post(self, request):
        # Lógica para crear un nuevo usuario
        pass

class UserDetail(View):
    def get(self, request, pk):
        user = get_object_or_404(User, pk=pk)
        return JsonResponse({'id': user.id, 'username': user.username, 'email': user.email, 'phone_number': user.phone_number})

    def put(self, request, pk):
        # Lógica para actualizar un usuario
        pass

    def delete(self, request, pk):
        # Lógica para eliminar un usuario
        pass

# Vistas para Artists
class ArtistList(View):
    def get(self, request):
        artists = list(Artists.objects.values())
        return JsonResponse(artists, safe=False)

    def post(self, request):
        # Lógica para crear un nuevo artista
        pass

class ArtistDetail(View):
    def get(self, request, pk):
        artist = get_object_or_404(Artists, pk=pk)
        return JsonResponse({'id': artist.id, 'name': artist.name})

    def put(self, request, pk):
        # Lógica para actualizar un artista
        pass

    def delete(self, request, pk):
        # Lógica para eliminar un artista
        pass

# Continúa de manera similar con los otros modelos
# Vistas para Events
class EventList(View):
    def get(self, request):
        events = list(Events.objects.values())
        return JsonResponse(events, safe=False)

    def post(self, request):
        # Lógica para crear un nuevo evento
        pass

class EventDetail(View):
    def get(self, request, pk):
        event = get_object_or_404(Events, pk=pk)
        return JsonResponse({'id': event.id, 'name': event.name, 'place': event.place, 'start_time': event.start_time})

    def put(self, request, pk):
        pass

    def delete(self, request, pk):
        pass


class MerchList(View):
    def get(self, request):
        merches = list(Merch.objects.values())
        return JsonResponse(merches, safe=False)

    def post(self, request):
        pass

class MerchDetail(View):
    def get(self, request, pk):
        merch = get_object_or_404(Merch, pk=pk)
        return JsonResponse({'id': merch.id, 'name': merch.name, 'price': merch.price, 'id_artist': merch.id_artist_id})

    def put(self, request, pk):
        pass

    def delete(self, request, pk):
        pass
'''