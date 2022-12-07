from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Music,Minus,History
from .service import qoshiqtext
from pathlib import Path
BASE_DIR = Path(__file__).resolve().parent.parent
import os 

@receiver(post_save,sender=Music)
def makeminus(sender,instance,created,**kwargs):
    if created:
        music = instance.music.url
        file_name = os.path.basename(music)
        filename = os.path.splitext(file_name)[0]
        import pydub
        data_music = qoshiqtext(filepath=f"{BASE_DIR}/{music}")
        singer_name = data_music['singer']
        song_name = data_music['song_name']
        c = Minus.objects.filter(singer_name=singer_name,song_name=song_name)
        if c.count()==0:
            filename = os.path.splitext(file_name)[0]
            os.system(f"spleeter separate -p spleeter:2stems -o {BASE_DIR}/media/output {BASE_DIR}/{music}")
            sound = pydub.AudioSegment.from_wav(f"{BASE_DIR}/media/output/{filename}/vocals.wav")
            sound.export(f"{BASE_DIR}/media/output/{filename}/vocals.mp3", format="mp3")
            sound = pydub.AudioSegment.from_wav(f"{BASE_DIR}/media/output/{filename}/accompaniment.wav")
            sound.export(f"{BASE_DIR}/media/output/{filename}/accompaniment.mp3", format="mp3")
            os.remove(f"{BASE_DIR}/media/output/{filename}/vocals.wav")
            os.remove(f"{BASE_DIR}/media/output/{filename}/accompaniment.wav")
            lyrics = data_music['lyrics']
            vocals = f"media/output/{filename}/vocals.mp3"
            accompaniment = f"media/output/{filename}/accompaniment.mp3"
            Minus.objects.create(
                music = instance,
                song_name = song_name,
                singer_name = singer_name,
                lyrics = lyrics,
                vocals = vocals,
                accompaniment = accompaniment
            )
            idminus = Minus.objects.filter(singer_name = singer_name ,song_name = song_name)
            History.objects.create(
                music=instance,
                minus = idminus[0],
                user = instance.user,
            )
        
        