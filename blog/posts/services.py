from .models import Post


def index_get_posts(request):
    posts = (
        Post.objects
        .select_related('author')
        .filter(status='published')
    )
    return posts
