from rest_framework import serializers
from .models import Music,Minus,History,Category,CategoryName


class MusicSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')
    class Meta:
        model = Music 
        fields = ['music','user']

class MinusSerializer(serializers.ModelSerializer):
    musicn = serializers.CharField(source='music.music')
    class Meta:
        model = Minus
        fields = ['musicn','vocals','accompaniment','singer_name','song_name','lyrics','background']


class SearchSerializer(serializers.ModelSerializer):
    class Meta:
        model=Minus
        fields = ['accompaniment','vocals','singer_name','song_name','music_img','background','lyrics']




class HistorySerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')
    music = serializers.CharField(source='music.music')
    vocals = serializers.CharField(source='minus.vocals')
    accompaniment = serializers.CharField(source='minus.accompaniment')
    singer_name = serializers.CharField(source = 'minus.singer_name')
    song_name = serializers.CharField(source='minus.song_name')
    lyrics = serializers.CharField(source='minus.lyrics')
    background = serializers.FileField(source='minus.background')
    music_img = serializers.CharField(source='minus.music_img')
    class Meta:
        model = History
        fields = ['music','vocals','user','accompaniment','singer_name','song_name','lyrics','background','music_img']




class MinusListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Minus
        fields = ['pk','vocals', 'accompaniment', 'singer_name', 'song_name', 'lyrics', 'background', 'music_img']

class KaraokeListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Minus
        fields = ['pk','vocals', 'accompaniment', 'singer_name', 'song_name', 'lyrics', 'background', 'music_img']

class CategorySerializer(serializers.ModelSerializer):
    singer_name = serializers.CharField(source = 'minus.singer_name')
    song_name = serializers.CharField(source='minus.song_name')
    music_img = serializers.CharField(source='minus.music_img')
    genre = serializers.CharField(source='genre.cat')
    duration = serializers.CharField(source = 'minus.duration')
    class Meta:
        model = Category
        fields = ['genre', 'singer_name', 'song_name', 'music_img', 'duration']


class CategoryNameListSerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoryName
        fields = ['pk','cat','cat_img']


class GetByIdSerializer(serializers.ModelSerializer):
    class Meta:
        model = Minus
        fields = ['vocals','accompaniment','singer_name','song_name','lyrics','background','music_img','duration']