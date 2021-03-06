from django.urls import path
from . import views

app_name = 'posts'

urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.post_create, name='post_create'),
    path('post/<int:post_id>-<slug:slug>/',
         views.post_detail, name='post_detail'),
    path('post/<int:post_id>-<slug:slug>/edit/',
         views.post_edit, name='post_edit'),
    path('post/<int:post_id>-<slug:slug>/like/',
         views.post_like, name='post_like'),
    path('post/<int:post_id>-<slug:slug>/dislike/',
         views.post_dislike, name='post_dislike'),
    path('post/<int:post_id>-<slug:slug>/comment/',
         views.post_comment, name='post_comment'),
    path('post/<int:post_id>-<slug:slug>/comment/<int:comment_id>/like/',
         views.comment_like, name='comment_like'),
    path('post/<int:post_id>-<slug:slug>/comment/<int:comment_id>/dislike/',
         views.comment_dislike, name='comment_dislike')
]
