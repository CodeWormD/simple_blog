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
    # получаем пост
    post = get_object_or_404(Post, id=post_id, slug=slug)
    # если лайк поставлен, то убираем лайк
    if PostLike.objects.filter(like_by=request.user, post=post).exists():
        PostLike.objects.filter(like_by=request.user, post=post).delete()
    # если поставлен дизлайк и нету лайка то
    elif PostDisLike.objects.filter(
        dislike_by=request.user,
        post=post
    ).exists() or PostLike.objects.filter(
        like_by=request.user,
        post=post
    ).exists() is False:
        # удаляем дизлайк и создаем лайк
        PostDisLike.objects.filter(dislike_by=request.user, post=post).delete()
        like, created = PostLike.objects.get_or_create(
            like_by=request.user,
            post_id=post_id
        )
        # если лайк не создался, то ставим значение дизлайк
        if not created:
            if like.value == 'Like':
                like.value = 'Dislike'
            else:
                like.value = 'Like'
        # сохраняем лайк
        return like.save()


def post_dislike_get(request, post_id, slug):
    post = get_object_or_404(Post, id=post_id, slug=slug)
    if PostDisLike.objects.filter(dislike_by=request.user, post=post).exists():
        PostDisLike.objects.filter(dislike_by=request.user, post=post).delete()
    elif PostLike.objects.filter(
        like_by=request.user,
        post=post
    ).exists() or PostDisLike.objects.filter(
        dislike_by=request.user,
        post=post
    ).exists() is False:
        PostLike.objects.filter(like_by=request.user, post=post).delete()
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
