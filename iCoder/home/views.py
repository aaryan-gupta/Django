from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from home.models import Contact
from blog.models import Post

# Create your views here.

def home(request):
	# return HttpResponse("This is home")
	return render(request, "home/home.html")

def contact(request):
	# messages.success(request, "Welcome to Contact")
	# messages.error(request, "Welcome to Contact")
	if request.method == "POST":
		name = request.POST["name"]
		email = request.POST["email"]
		phone = request.POST["phone"]
		content = request.POST["content"]
		if len(name) < 2 or len(email) < 3 or len(phone) < 10 or len(content) < 4:
			messages.error(request, "Please fill the form correctly.")
		else:
			contact = Contact(name=name, email=email, phone=phone, content=content)
			contact.save()
			messages.success(request, "Your message has been successfully sent.")
			return redirect("/contact")
	return render(request, "home/contact.html")

def about(request):
	""" messages.success(request, "This is About")
	messages.error(request, "This is About") """
	return render(request, "home/about.html")

def search(request):
	query = request.GET["query"]
	# allPosts = Post.objects.all()
	allPosts = Post.objects.filter(title__icontains=query)
	params = {"allPosts": allPosts}
	return render(request, "home/search.html", params)
	# return HttpResponse("Search")