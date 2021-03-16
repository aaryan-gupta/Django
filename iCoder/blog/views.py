from django.shortcuts import render, HttpResponse
from blog.models import Post

# Create your views here.

def blogHome(request):
	# return HttpResponse("This is blogHome. We will keep all the blog posts here.")
	allPosts = Post.objects.all()
	context = {"allPosts": allPosts}
	return render(request, "blog/blogHome.html", context)

def blogPost(request, slug):
	# return HttpResponse(f"This is blogPost: {slug}")
	return render(request, "blog/blogPost.html")