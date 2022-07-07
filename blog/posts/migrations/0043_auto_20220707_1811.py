# Generated by Django 2.2.16 on 2022-07-07 15:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('posts', '0042_auto_20220704_1516'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ['title', '-pub_date', 'pk'], 'verbose_name': 'пост', 'verbose_name_plural': 'посты'},
        ),
        migrations.CreateModel(
            name='CommentDisLike',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.CharField(choices=[('Like', 'Like'), ('Dislike', 'Dislike')], default='Dislike', max_length=10, verbose_name='Дизлайк')),
                ('comment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='commentdislikes', to='posts.Comment', verbose_name='Дизайк коммента')),
                ('dislike_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='commentdislikes', to=settings.AUTH_USER_MODEL, verbose_name='Автор дизлайка коммента')),
            ],
            options={
                'verbose_name': 'Дизлайк комментария',
                'verbose_name_plural': 'Дизлайк комментариев',
            },
        ),
    ]
