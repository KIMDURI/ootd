# Generated by Django 2.1.4 on 2018-12-20 16:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0004_auto_20181215_1432'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='like_user_set',
        ),
        migrations.AddField(
            model_name='post',
            name='photo',
            field=models.ImageField(blank=True, upload_to='post/%Y/%m/%d'),
        ),
    ]