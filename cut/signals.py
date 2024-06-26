import string
import random
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import CutMusic,JoinMusic,VolumeMix
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
def join_musics1(sender,instance,created,**kwargs):
    if created:
        first_music = f"{BASE_DIR}{instance.first_music}"
        second_music = f"{BASE_DIR}{instance.second_music.url}"

        sound1 = AudioSegment.from_mp3(first_music)
        sound2 = AudioSegment.from_mp3(second_music)
        output = sound1.overlay(sound2)

        file_name = ''.join(random.choices(string.ascii_lowercase, k=20))
        file_name = f"{file_name}.mp3"
        folder_name = f"mixed/{file_name}"
        output.export(f"{BASE_DIR}/media/{folder_name}",format='mp3')
        instance.mixed_music = folder_name
        instance.save()


@receiver(post_save, sender=VolumeMix)
def join_musics(sender, instance, created, **kwargs):
    if created:
        first_music = f"{BASE_DIR}/{instance.instrumental}"
        second_music = f"{BASE_DIR}/{instance.vocals}"
        vocals_percent = instance.vocals_percent
        instrumental_percent = instance.instrumental_percent
        sound1 = AudioSegment.from_mp3(first_music)
        sound2 = AudioSegment.from_mp3(second_music)
        sound1 = sound1-(40-instrumental_percent*0.4)
        sound2 = sound2-(50-vocals_percent*0.4)
        output = sound1.overlay(sound2)
        file_name = ''.join(random.choices(string.ascii_lowercase, k=20))
        file_name = f"{file_name}.mp3"
        folder_name = f"mixed/{file_name}"
        
        
        output.export(f"{BASE_DIR}/media/{folder_name}", format='mp3')
        instance.joined_music = folder_name
        instance.save()
        
        



