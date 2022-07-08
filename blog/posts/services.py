from .models import (Post, PostLike, PostDisLike,
                     Comment, CommentLike, CommentDisLike)
from django.shortcuts import get_object_or_404


def index_get_posts(request):
    posts = (
        Post.published
        .select_related('author')
    )
    return posts


def get_post_or_404(post_id, slug):
    post = get_object_or_404(Post, pk=post_id, slug=slug)
    return post


def post_like_get(request, post_id, slug):
    post = get_object_or_404(Post, id=post_id, slug=slug)
    post_like = PostLike.objects.filter(like_by=request.user, post=post)
    post_dis = PostDisLike.objects.filter(
        dislike_by=request.user,
        post=post
    )
    if post_like.exists():
        post_like.delete()
    elif post_dis.exists() or post_like.exists() is False:
        post_dis.delete()
        like, created = PostLike.objects.get_or_create(
            like_by=request.user,
            post_id=post_id
        )
        if not created:
            if like.value == 'Like':
                like.value = 'Dislike'
            else:
                like.value = 'Like'
        return like.save()


def post_dislike_get(request, post_id, slug):
    post = get_object_or_404(Post, id=post_id, slug=slug)
    post_like = PostLike.objects.filter(like_by=request.user, post=post)
    post_dis = PostDisLike.objects.filter(
        dislike_by=request.user,
        post=post
    )
    if post_dis.exists():
        post_dis.delete()
    elif post_like.exists() or post_dis.exists() is False:
        post_like.delete()
        dislike, created = PostDisLike.objects.get_or_create(
            dislike_by=request.user,
            post_id=post_id
        )
        if not created:
            if dislike.value == 'Dislike':
                dislike.value = 'Like'
            else:
                dislike.value = 'Dislike'
        return dislike.save()


def comment_like_get(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)
    com_like = CommentLike.objects.filter(
        like_by=request.user,
        comment=comment)
    com_dislike = CommentDisLike.objects.filter(
        dislike_by=request.user,
        comment=comment)
    if com_like.exists():
        com_like.delete()
    elif com_dislike.exists() or com_like.exists() is False:
        com_dislike.delete()
        like, created = CommentLike.objects.get_or_create(
            like_by=request.user,
            comment=comment
        )
        if not created:
            if like.value == 'Like':
                like.value == 'Dislike'
            else:
                like.value == 'Like'
        return like.save()


def comment_dislike_get(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)
    com_like = CommentLike.objects.filter(
        like_by=request.user,
        comment=comment
    )
    com_dislike = CommentDisLike.objects.filter(
        dislike_by=request.user,
        comment=comment
    )
    if com_dislike.exists():
        com_dislike.delete()
    elif com_like.exists() or com_dislike.exists() is False:
        com_like.delete()
        dislike, created = CommentDisLike.objects.get_or_create(
            dislike_by=request.user,
            comment=comment
        )
        if not created:
            if dislike.values == 'Dislike':
                dislike.values = 'Like'
            else:
                dislike.values = 'Dislike'
        return dislike.save()
