from django.contrib import admin

from .models import Comment, Post, CommentLikes, Follow


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = (
        'pk',
        'title',
        'description',
        'text',
        'author',
        'created',
        'pub_date',
        'update',
        'status'
    )
    search_fields = ('title',)
    list_filter = ('pub_date', 'title')
    empty_value_display = '-пусто-'


@admin.register(Comment)
class Comment(admin.ModelAdmin):
    list_display = (
        'post',
        'author'
        
    )


@admin.register(CommentLikes)
class CommentLikes(admin.ModelAdmin):
    list_display = (
        'post',
        'like_by'
    )
    
    
@admin.register(Follow)
class Follow(admin.ModelAdmin):
    list_display = (
        'user',
        'author'
    )