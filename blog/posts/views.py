from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import get_user_model
from .models import Post
from .services import index_get_posts, post_detail_get_post
from .forms import PostForm

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


def post_edit(request, slug, post_id):
    post = get_object_or_404(Post, slug=slug, id=post_id)
    if post.author != request.user:
        return redirect('posts:post_detail', post_id, slug)
    form = PostForm(
        request.POST or None,
        files=request.FILES or None,
        instance=post
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
