# Generated by Django 2.2.16 on 2022-06-30 18:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0024_auto_20220630_2142'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='disliked',
        ),
    ]
