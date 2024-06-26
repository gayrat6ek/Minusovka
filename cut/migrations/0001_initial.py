# Generated by Django 3.2.16 on 2022-12-12 05:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CutMusic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cutting_music', models.FileField(upload_to='cut_music/')),
                ('cutted_music', models.FileField(blank=True, max_length=255, null=True, upload_to='')),
                ('time_from', models.BigIntegerField(blank=True, default=0, null=True)),
                ('time_to', models.BigIntegerField(blank=True, default=30000, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='JoinMusic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_music', models.FileField(upload_to='documents/%Y/%m/%d')),
                ('second_music', models.FileField(upload_to='documents/%Y/%m/%d')),
                ('mixed_music', models.FileField(blank=True, null=True, upload_to='')),
            ],
        ),
    ]
