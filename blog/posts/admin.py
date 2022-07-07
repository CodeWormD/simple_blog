from django.contrib import admin

from .models import (
    Comment, Post,
    CommentLike, Follow, PostLike,
    PostDisLike, CommentDisLike
    )


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = (
        'pk',
        'title',
        'author',
        'created',
        'pub_date',
        'update',
        'status'
    )
    search_fields = ('title',)
    list_filter = ('pub_date', 'title', 'id')
    empty_value_display = '-пусто-'


@admin.register(Comment)
class Comment(admin.ModelAdmin):
    list_display = (
        'post',
        'author'
    )


@admin.register(CommentLike)
class CommentLikes(admin.ModelAdmin):
    list_display = (
        'comment',
        'like_by',
        'value'
    )


@admin.register(CommentDisLike)
class CommentDisLikes(admin.ModelAdmin):
    list_display = (
        'comment',
        'dislike_by',
        'value'
    )


@admin.register(PostLike)
class PostLikes(admin.ModelAdmin):
    list_display = (
        'post',
        'like_by',
        'value'
    )


@admin.register(PostDisLike)
class PostDisLikes(admin.ModelAdmin):
    list_display = (
        'post',
        'dislike_by',
        'value'
    )


@admin.register(Follow)
class Follow(admin.ModelAdmin):
    list_display = (
        'user',
        'author'
    )
