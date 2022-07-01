# Generated by Django 2.2.16 on 2022-06-30 19:37

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0030_auto_20220630_2235'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='disliked',
            field=models.ManyToManyField(related_name='posts_disliked', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='post',
            name='liked',
            field=models.ManyToManyField(related_name='posts_liked', to=settings.AUTH_USER_MODEL),
        ),
    ]
