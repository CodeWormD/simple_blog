from .models import Post, PostLike, PostDisLike
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
