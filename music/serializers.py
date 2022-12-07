from rest_framework import serializers
from .models import Music,Minus,History


class MusicSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')
    class Meta:
        model = Music 
        fields = ['music','user']

class MinusSerializer(serializers.ModelSerializer):
    musicn = serializers.CharField(source='music.music')
    class Meta:
        model = Minus
        fields = ['musicn','vocals','accompaniment','singer_name','song_name','lyrics']

class HistorySerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')
    music = serializers.CharField(source='music.music')
    vocals = serializers.CharField(source='minus.vocals')
    accompaniment = serializers.CharField(source='minus.accompaniment')
    singer_name = serializers.CharField(source = 'minus.singer_name')
    song_name = serializers.CharField(source='minus.song_name')
    lyrics = serializers.CharField(source='minus.lyrics')
    class Meta:
        model = History
        fields = ['music','vocals','user','accompaniment','singer_name','song_name','lyrics']
