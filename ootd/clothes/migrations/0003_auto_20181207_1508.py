# Generated by Django 2.1.4 on 2018-12-07 15:08

import clothes.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clothes', '0002_auto_20181207_1335'),
    ]

    operations = [
        migrations.AlterField(
            model_name='thumb_closet',
            name='thumb',
            field=models.ImageField(upload_to=clothes.models.Thumb_closet.path),
        ),
    ]
