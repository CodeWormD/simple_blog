# Generated by Django 2.2.16 on 2022-07-01 07:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0039_auto_20220701_0948'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='disliked',
        ),
        migrations.RemoveField(
            model_name='post',
            name='liked',
        ),
    ]