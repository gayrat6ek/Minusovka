from rest_framework import serializers
from .models import CutMusic

class Cutserializer(serializers.ModelSerializer):
    cutted_music = serializers.FileField(read_only=True)
    class Meta:
        model = CutMusic
        fields = ['time_from', 'time_to','cutting_music','cutted_music']