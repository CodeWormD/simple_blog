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
]
