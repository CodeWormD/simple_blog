# Generated by Django 2.2.16 on 2022-06-26 17:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0005_auto_20220626_2026'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='commentlikes',
            options={'verbose_name': 'Лайк комментария', 'verbose_name_plural': 'Лайки комментариев'},
        ),
        migrations.AlterModelOptions(
            name='postlikes',
            options={'verbose_name': 'Лайк поста', 'verbose_name_plural': 'Лайки постов'},
        ),
        migrations.AlterField(
            model_name='commentlikes',
            name='like',
            field=models.BooleanField(verbose_name='Лайк'),
        ),
        migrations.AlterField(
            model_name='postlikes',
            name='like',
            field=models.BooleanField(verbose_name='Лайк'),
        ),
    ]