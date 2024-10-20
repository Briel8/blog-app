from django.shortcuts import render

def index(request):
    return render(request, "Blog_App/index.html")

def detail(request, post_id):
    pass