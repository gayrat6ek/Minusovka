# Generated by Django 3.2.16 on 2022-12-22 11:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0010_userobject'),
    ]

    operations = [
        migrations.CreateModel(
            name='SampleBackground',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('background', models.FileField(upload_to='')),
            ],
        ),
    ]