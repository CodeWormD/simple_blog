from django.db import models
from django.conf import settings
from django.utils import timezone
from django.contrib.auth import get_user_model
# from django.utils.text import slugify
from pytils.translit import slugify


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
    slug = models.SlugField(
        blank=True,
        null=True
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

    # почекать как будет отображаться self.id в урлах
    def save(self, *args, **kwargs):
        self.slug = slugify(f'{self.id}-{self.title}')
        super().save(*args, **kwargs)

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
        related_name='comments',
        on_delete=models.CASCADE,

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
    comment = models.ForeignKey(
        Comment,
        verbose_name='Лайк коммента',
        related_name='commentlikes',
        on_delete=models.CASCADE
    )
    like_by = models.ForeignKey(
        User,
        verbose_name='Автор лайка коммента',
        related_name='commentlikes',
        on_delete=models.SET_NULL,
        null=True
    )
    like = models.BooleanField(
        verbose_name='Лайк',
    )
    created = models.DateTimeField(
        verbose_name='Время создания',
        auto_now_add=True
    )

    class Meta:
        verbose_name = 'Лайк комментария'
        verbose_name_plural = 'Лайки комментариев'

    def __str__(self):
        return str(self.like_by)


class PostLikes(models.Model):
    post = models.ForeignKey(
        Post,
        verbose_name='Лайк поста',
        related_name='postlikes',
        on_delete=models.CASCADE
    )
    like_by = models.ForeignKey(
        User,
        verbose_name='Автор лайка поста',
        related_name='postlikes',
        on_delete=models.CASCADE
    )
    like = models.BooleanField(
        verbose_name='Лайк'
    )
    created = models.DateTimeField(
        verbose_name='Время лайка',
        auto_now_add=True
    )

    class Meta:
        verbose_name = 'Лайк поста'
        verbose_name_plural = 'Лайки постов'

    def __str__(self):
        return str(self.like_by)


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
