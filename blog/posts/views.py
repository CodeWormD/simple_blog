from django.shortcuts import render  # , get_object_or_404
from django.contrib.auth import get_user_model
# from .models import Post
from .services import index_get_posts

User = get_user_model()


def index(request):
    context = {
        'posts': index_get_posts(request)
    }
    return render(request, 'posts/index.html', context)
