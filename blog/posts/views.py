from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import get_user_model
from .models import Comment, CommentLike, CommentDisLike
from django.http import JsonResponse, HttpResponse
from .services import (
    index_get_posts, get_post_or_404, post_like_get, post_dislike_get)
from .forms import PostForm, CommentForm

User = get_user_model()


def index(request):
    context = {
        'posts': index_get_posts(request)
    }
    return render(request, 'posts/index.html', context)


def post_detail(request, post_id, slug):
    form = CommentForm(request.POST or None)
    context = {
        'post': get_post_or_404(post_id, slug),
        'form': form
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


def post_comment(request, post_id, slug):
    post = get_post_or_404(post_id, slug)
    form = CommentForm(
        request.POST or None
    )
    if form.is_valid():
        comment = form.save(commit=False)
        comment.author = request.user
        comment.post = post
        comment.save()
    else:
        return redirect('posts:index')
    return redirect('posts:post_detail', post_id, slug)


def comment_like(request, post_id, slug, comment_id):
    if request.user.is_authenticated:
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
            like.save()
    else:
        return redirect('posts:index')
    return redirect('posts:post_detail', post_id, slug)
