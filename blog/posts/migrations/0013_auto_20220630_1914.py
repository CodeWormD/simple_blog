# Generated by Django 2.2.16 on 2022-06-30 16:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('posts', '0012_auto_20220630_1749'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='disliked',
        ),
        migrations.AddField(
            model_name='post',
            name='disliked',
            field=models.ForeignKey(blank=True, default=None, on_delete=django.db.models.deletion.CASCADE, related_name='postsunlike', to=settings.AUTH_USER_MODEL),
        ),
        migrations.RemoveField(
            model_name='post',
            name='liked',
        ),
        migrations.AddField(
            model_name='post',
            name='liked',
            field=models.ForeignKey(blank=True, default=None, on_delete=django.db.models.deletion.CASCADE, related_name='postslike', to=settings.AUTH_USER_MODEL),
        ),
    ]
