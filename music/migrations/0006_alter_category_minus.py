# Generated by Django 3.2.16 on 2022-12-17 08:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0005_alter_category_genre'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='minus',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='music.minus', unique=True),
        ),
    ]
