# Generated by Django 3.2.16 on 2022-12-17 08:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0006_alter_category_minus'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='minus',
            field=models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to='music.minus'),
        ),
    ]
