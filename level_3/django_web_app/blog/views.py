from django.shortcuts import render, HttpResponse
from .models import Post
# Create your views here.

def home(request):
    return render(request, 'home.html')

def posts(request):
    all_post = Post.objects.all().order_by('-created_at', 'title')
    return render(request, 'posts.html', {'posts': all_post})