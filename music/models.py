from django.db import models
from django.conf import settings
User = settings.AUTH_USER_MODEL
# Create your models here.
class Music(models.Model):
    music = models.FileField(upload_to='documents/%Y/%m/%d')
    moment = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.moment.hour} : {self.moment.minute}"
    class Meta:
        ordering = ['-moment']

class Minus(models.Model):
    music = models.ForeignKey(Music,on_delete=models.CASCADE,null=True,blank=True)
    vocals = models.CharField(max_length=250)
    accompaniment = models.CharField(max_length=250)
    song_name = models.CharField(max_length=250,null=True,blank=True)
    singer_name = models.CharField(max_length=250,null=True,blank=True)
    background = models.FileField(upload_to='documents/%Y/%m/%d',default='documents/green.mp4')
    user = models.CharField(User,max_length=250)
    lyrics = models.TextField(null=True,blank=True)
    time_created = models.DateTimeField(auto_now_add=True)
    music_img = models.TextField(default='media/documents/naushnik.jpg')


class History(models.Model):
    music = models.ForeignKey(Music,on_delete=models.PROTECT)
    minus = models.ForeignKey(Minus,on_delete=models.PROTECT)
    user = models.CharField(User,max_length=150)
    time_created = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.user
    class Meta:
        ordering=['-time_created']