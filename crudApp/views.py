from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from crudApp.models import Post

# Create your views here.
def index(request):
	posts = Post.objects.all()
	return render(request, 'index.html', {'posts': posts})

def post_detail(request, pk):
	post = get_object_or_404(Post, pk=pk)
	return render(request, 'post_detail.html', {'post': post})

def sign_in(request):
	return render(request, 'signin.html', {})

def sign_up(request):
	return render(request, 'signup.html', {})