# Generated by Django 2.2.16 on 2022-06-30 19:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0028_auto_20220630_2224'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='dislllliked',
            new_name='disliked',
        ),
    ]
