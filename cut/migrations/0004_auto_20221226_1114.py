# Generated by Django 3.2.16 on 2022-12-26 06:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cut', '0003_volumemix'),
    ]

    operations = [
        migrations.AlterField(
            model_name='volumemix',
            name='instrumental',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='volumemix',
            name='vocals',
            field=models.CharField(max_length=255),
        ),
    ]
