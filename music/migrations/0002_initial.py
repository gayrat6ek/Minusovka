# Generated by Django 3.2.16 on 2022-12-08 05:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('music', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='music',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='minus',
            name='music',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='music.music'),
        ),
        migrations.AddField(
            model_name='history',
            name='minus',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='music.minus'),
        ),
        migrations.AddField(
            model_name='history',
            name='music',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='music.music'),
        ),
    ]