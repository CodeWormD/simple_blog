# Generated by Django 2.2.16 on 2022-06-30 14:49

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('posts', '0011_auto_20220630_1747'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='DisLikes',
            new_name='PostDisLikes',
        ),
    ]