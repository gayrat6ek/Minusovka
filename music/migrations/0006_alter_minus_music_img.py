# Generated by Django 3.2.16 on 2022-12-10 10:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0005_alter_minus_music_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='minus',
            name='music_img',
            field=models.CharField(blank=True, default='media/documents/2022/12/07/naushnik.jpg', max_length=255, null=True),
        ),
    ]
