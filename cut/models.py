from django.db import models

# Create your models here.
class CutMusic(models.Model):
    cutting_music = models.FileField(upload_to='cut_music/')
    cutted_music= models.FileField(max_length=255,null=True,blank=True)
    time_from = models.FloatField(null=True,blank=True,default=0)
    time_to = models.FloatField(null=True,blank=True,default=30000)
class JoinMusic(models.Model):
    first_music = models.FileField(upload_to='documents/%Y/%m/%d')
    second_music = models.FileField(upload_to='documents/%Y/%m/%d')
    mixed_music = models.FileField(null=True,blank=True)
    