from urllib.parse import uses_fragment
from django.db import models
from django.conf import settings
from django.utils import timezone
from django.contrib.auth import get_user_model


User = get_user_model()


class Post(models.Model):
    DRAFT = 'draft'
    PUBLISHED = 'published'
    STATUS_CHOISE = (
        (DRAFT, 'Draft'),
        (PUBLISHED, 'Published'),
    )
    title = models.TextField(
        verbose_name='Заголовок',
        help_text='Заголовок', 
        max_length=100,
        unique=True
    )
    description = models.TextField(
        verbose_name='Описание',
        help_text='Описание',
        max_length=100,
        null=True,
        blank=True,
        unique=True
    )
    text = models.TextField(
        verbose_name='Текст поста',
        help_text='Текст поста',

    )
    author = models.ForeignKey(
        User,
        verbose_name='Автор',
        on_delete=models.CASCADE,
        related_name='posts',
    )
    created = models.DateTimeField(
        verbose_name='Дата создания',
        auto_now_add=True
    )
    pub_date = models.DateTimeField(
        verbose_name='Дата публикации',
        default=timezone.now)
    update = models.DateTimeField(
        verbose_name='Время Редактирования',
        auto_now=True
    )
    status = models.CharField(
        max_length=15,
        choices=STATUS_CHOISE,
        default=DRAFT        
    )
    image = models.ImageField(
        verbose_name='Картинка',
        upload_to='posts/',
        blank=True
    )

    
    class Meta:
        ordering = ['title', '-pub_date']
        verbose_name = 'пост'
        verbose_name_plural = 'посты'

    def __str__(self):
        return self.title and self.text[:settings.TEXT_ADMIN_SHOW]

    
    
class Comment(models.Model):
    post = models.ForeignKey(
        Post,
        verbose_name='Пост комментария',
        related_name='comments',
        on_delete=models.CASCADE
    )
    text = models.TextField(
        verbose_name='Текст комментария',
        help_text='Текст комментария',
        max_length=100
    )
    author = models.ForeignKey(
        User,
        verbose_name='Автор комментария',
        on_delete=models.CASCADE,
        related_name='comments'
    )
    created = models.DateTimeField(
        verbose_name='Дата создания',
        auto_now_add=True
    )
    
    class Meta:
        verbose_name = 'комментарий'
        verbose_name_plural = 'комментарии'
    
    def __str__(self):
        return self.author and self.text[:settings.TEXT_ADMIN_SHOW]
        


class CommentLikes(models.Model):
    post = models.ForeignKey(
        Post,
        verbose_name='Лайк поста',
        related_name='commentlikes',
        on_delete=models.CASCADE
    )
    like_by = models.ForeignKey(
        User,
        verbose_name='Поставил лайк',
        on_delete=models.SET_NULL,
        null=True
    )
    like = models.IntegerField(
        verbose_name='Лайк',
    )
    created = models.DateTimeField(
        verbose_name='Время создания',
        auto_now_add=True
    )
    
    class Meta:
        verbose_name = 'Лайк'
        verbose_name_plural = 'Лайки'    



class Follow(models.Model):
    user = models.ForeignKey(
        User,
        verbose_name='Подписчик',
        related_name='follower',
        on_delete=models.CASCADE
    )
    author = models.ForeignKey(
        User,
        verbose_name='На кого подписываются',
        related_name='following',
        on_delete=models.CASCADE
    )

    class Meta:
        verbose_name = 'Подписка'
        verbose_name_plural = 'Подписки'

    def __str__(self):
        return f'{self.user} подписался на {self.author}'