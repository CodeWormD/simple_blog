from django.urls import path
from . import views

app_name = 'posts'

urlpatterns = [
    path('', views.index, name='index'),
    path('post/<int:post_id>-<slug:slug>/',
         views.post_detail, name='post_detail'),
]
