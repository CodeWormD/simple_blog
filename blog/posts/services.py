from .models import Post
from django.shortcuts import get_object_or_404


def index_get_posts(request):
    posts = (
        Post.objects
        .select_related('author')
    )
    return posts


def post_detail_get_post(post_id, slug):
    post = get_object_or_404(Post, pk=post_id, slug=slug)
    return post


def post_edit_get_post(slug, post_id):
    pass
