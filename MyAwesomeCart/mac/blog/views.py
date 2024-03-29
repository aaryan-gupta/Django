from django.shortcuts import render
from django.http import HttpResponse
from .models import Blogpost

# Create your views here.

def index(request):
	# return HttpResponse("Index Blog")
	myposts = Blogpost.objects.all()
	return render(request, "blog/index.html", {"myposts": myposts})

def blogpost(request, pid):
	post = Blogpost.objects.filter(post_id = pid)[0]
	return render(request, "blog/blogpost.html", {"post": post})