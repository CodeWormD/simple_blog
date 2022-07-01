from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import get_user_model
from .models import Post, PostLike, PostDisLike
from .services import index_get_posts, get_post_or_404, post_like_get, post_dislike_get
from .forms import PostForm

User = get_user_model()


def index(request):
    context = {
        'posts': index_get_posts(request)
    }
    return render(request, 'posts/index.html', context)


def post_detail(request, post_id, slug):
    context = {
        'post': get_post_or_404(post_id, slug)
    }
    return render(request, 'posts/post_detail.html', context)


def post_edit(request, post_id, slug):
    if get_post_or_404(post_id, slug).author != request.user:
        return redirect('posts:post_detail', post_id, slug)
    form = PostForm(
        request.POST or None,
        files=request.FILES or None,
        instance=get_post_or_404(post_id, slug)
    )
    if form.is_valid():
        form.save()
        return redirect('posts:index')
    context = {
        'form': form
    }
    return render(request, 'posts/post_create.html', context)


def post_create(request):
    form = PostForm(
        request.POST or None,
        files=request.FILES or None,
    )
    context = {
        'form': form
    }
    if not form.is_valid():
        return render(request, 'posts/post_create.html', context)
    post = form.save(commit=False)
    post.author = request.user
    post.save()
    return redirect('posts:index')


def post_like(request, post_id, slug):
    post_like_get(request, post_id, slug)
    return redirect('posts:index')


def post_dislike(request, post_id, slug):
    post_dislike_get(request, post_id, slug)
    return redirect('posts:index')
