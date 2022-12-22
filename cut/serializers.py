from rest_framework import serializers
from .models import CutMusic,JoinMusic,VolumeMix

class Cutserializer(serializers.ModelSerializer):
    cutted_music = serializers.FileField(read_only=True)
    class Meta:
        model = CutMusic
        fields = ['time_from', 'time_to','cutting_music','cutted_music']
    def create(self, validated_data):
        return super().create(validated_data)

class MixMusicSerializer(serializers.ModelSerializer):
    mixed_music = serializers.FileField(read_only=True)
    class Meta:
        model=JoinMusic
        fields = ['first_music','second_music','mixed_music']


class VolumeMixSerializer(serializers.ModelSerializer):
    joined_music = serializers.FileField(read_only=True)
    class Meta:
        model = VolumeMix
        fields = ['instrumental', 'vocals','instrumental_percent', 'vocals_percent', 'joined_music']
