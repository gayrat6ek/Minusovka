# Generated by Django 3.2.16 on 2022-12-17 10:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0008_category_cat_img'),
    ]

    operations = [
        migrations.CreateModel(
            name='CategoryName',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cat', models.CharField(max_length=255)),
                ('cat_img', models.ImageField(upload_to='documents/%Y/%m/%d')),
            ],
        ),
        migrations.RemoveField(
            model_name='category',
            name='cat_img',
        ),
        migrations.AlterField(
            model_name='category',
            name='genre',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='music.categoryname'),
        ),
    ]