from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import CutMusic,JoinMusic
from pydub import AudioSegment
from pathlib import Path
import pathlib
import os
BASE_DIR = Path(__file__).resolve().parent.parent

@receiver(post_save,sender=CutMusic)
def makeminus(sender,instance,created,**kwargs):
    if created:
        music_url = f"{BASE_DIR}{instance.cutting_music.url}"
        StrtTime = instance.time_from
        EndTime = instance.time_to
        sound = AudioSegment.from_mp3(music_url)
        extract = sound[StrtTime:EndTime]
        filename = os.path.basename(instance.cutting_music.url)
        filename = f"/media/cutted/{filename}"
        export_url = f"{BASE_DIR}{filename}"

        extract.export(export_url, format="mp3")

        instance.cutted_music = filename.replace('media','')
        instance.save()


@receiver(post_save,sender=JoinMusic)
def join_musics(sender,instance,created,**kwargs):
    if created:
        first_music = f"{BASE_DIR}{instance.first_music.url}"
        second_music = f"{BASE_DIR}{instance.second_music.url}"

        sound1 = AudioSegment.from_mp3(first_music)
        sound2 = AudioSegment.from_mp3(second_music)
        output = sound1.overlay(sound2)

        file_name = os.path.basename(instance.first_music.url)
        folder_name = f"mixed/{file_name}"
        print(folder_name)
        output.export(f"{BASE_DIR}/media/{folder_name}",format='mp3')
        instance.mixed_music = folder_name
        instance.save()


