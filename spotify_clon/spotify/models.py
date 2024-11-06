from django.db import models

# Create your models here.

class User(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=150, unique=True,null=False, blank=False)
    email = models.EmailField(unique=True,null=False, blank=False)
    phone_number = models.CharField(max_length=15, unique=True,null=False, blank=False)
    password = models.CharField(max_length=128,null=False, blank=False)
    
    def __str__(self):
        return self.username
    
    class Meta:
        db_table = 'users'
        verbose_name = 'user'
        verbose_name_plural = 'users'
        ordering = ['id']
        
class Artists(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=150,null=False, blank=False)
    def __str__(self):
        return self.name
    
    class Meta:
        db_table = 'artists'
        verbose_name = 'artist'
        verbose_name_plural = 'artists'
        ordering = ['id']
        
class Events(models.Model):
    id= models.AutoField(primary_key=True)
    name = models.CharField(max_length=150,null=False, blank=False)
    place = models.CharField(max_length=150,null=False, blank=False)
    start_time = models.TimeField(null=False, blank=False)
    
    def __str__(self):
        return self.name
    class Meta:
        db_table = 'events'
        verbose_name = 'event'
        verbose_name_plural = 'events'
        ordering = ['id']

class EventsxArtist(models.Model):
    id= models.AutoField(primary_key=True)
    id_event = models.ForeignKey(Events,on_delete= models.CASCADE)
    id_artist = models.ForeignKey(Artists,on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name
    class Meta:
        db_table = 'eventxartists'
        verbose_name = 'eventxartist'
        verbose_name_plural = 'eventxartists'
        ordering = ['id']
        
class Merch(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=150,null=False, blank=False)
    price = models.DecimalField(max_digits=10, decimal_places=2,null=False, blank=False)
    id_artist = models.ForeignKey(Artists,on_delete= models.CASCADE) 
    def __str__(self):
        return self.name
    class Meta:
        db_table = 'merchs'
        verbose_name = 'merch'
        verbose_name_plural = 'merches'
        ordering = ['id']
      
class ArtistsXSongs(models.Model):
    id = models.AutoField(primary_key=True)
    id_artist = models.ForeignKey(Artists,on_delete= models.CASCADE)
    class Meta:
        db_table ='artistsxsongs'
        verbose_name = 'artistxsong'
        verbose_name_plural = 'artistsxsongs'
        ordering = ['id']
class Songs(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=150,null=False, blank=False)
    file = = models.FileField(upload_to='docs/')
    def __str__(self):
        return self.name
    
    class Meta:
        db_table = 'songs'
        verbose_name = 'song'
        verbose_name_plural = 'songs'
        ordering = ['id']
             
class Playlists(models.Model):
    id = models.AutoField(primary_key=True) 
    name = models.CharField(max_length=150,null=False, blank=False)  
    description = models.CharField(max_length=500)
    id_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='id_users')
    def __str__(self):
        return self.name
    
    class Meta:
        db_table = 'playlists'
        verbose_name = 'playlist'
        verbose_name_plural = 'playlists'
        ordering = ['id']
        
class SongsXlists(models.Model):
    id= models.AutoField(primary_key=True)
    id_song = models.ForeignKey(Songs,on_delete= models.CASCADE)
    id_playlist = models.ForeignKey(Playlists,on_delete = models.CASCADE)

    class Meta:
        db_table = 'songsxlists'
        verbose_name = 'songxlist'
        verbose_name_plural = 'songsxlists'
        ordering = ['id']
       
class Tags(models.Model):
    id = models.AutoField(primary_key=True)
    content = models.CharField(max_length=150,null=False, blank=False)
    class Meta :
        db_table = 'tags'
        verbose_name = 'tag'
        verbose_name_plural = 'tags'
        ordering = ['id']

class TagsxSongs(models.Model):
    id = models.AutoField(primary_key=True)
    id_song = models.ForeignKey(Songs,on_delete= models.CASCADE)
    id_tag = models.ForeignKey(Tags,on_delete= models.CASCADE)