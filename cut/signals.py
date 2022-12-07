from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import CutMusic
from pydub import AudioSegment
from pathlib import Path
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

