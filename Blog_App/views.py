from django.shortcuts import get_object_or_404, render
from .models import Post

def index(request):
    posts = Post.objects.all()
    context = {'posts': posts}
    return render(request, "Blog_App/index.html", context)

def detail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    context = {'post': post}
    return render(request, "Blog_App/detail.html", context)