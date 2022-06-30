from .models import Post
from django.shortcuts import get_object_or_404


def index_get_posts(request):
    posts = (
        Post.objects
        .select_related('author')
    )
    return posts


def get_post_or_404(post_id, slug):
    post = get_object_or_404(Post, pk=post_id, slug=slug)
    return post
