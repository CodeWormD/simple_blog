from django.shortcuts import render  # , get_object_or_404
from django.contrib.auth import get_user_model
# from .models import Post
from .services import index_get_posts, post_detail_get_post

User = get_user_model()


def index(request):
    context = {
        'posts': index_get_posts(request)
    }
    return render(request, 'posts/index.html', context)


def post_detail(request, slug, post_id):
    context = {
        'post': post_detail_get_post(post_id, slug)
    }
    return render(request, 'posts/post_detail.html', context)
