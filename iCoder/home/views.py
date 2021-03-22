from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from home.models import Contact
from blog.models import Post
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

# Create your views here.

def home(request):
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
	if len(query) > 78:
		allPosts = Post.objects.none()
	else:
		# allPosts = Post.objects.all()
		allPostsTitle = Post.objects.filter(title__icontains=query)
		allPostsContent = Post.objects.filter(content__icontains=query)
		allPosts = allPostsTitle.union(allPostsContent)
	if allPosts.count() == 0:
		messages.warning(request, "No search results found. Please refine your query.")
	params = {"allPosts": allPosts, "query": query}
	return render(request, "home/search.html", params)
	# return HttpResponse("Search")

def handleSignup(request):
	if request.method == "POST":
		# GET THE POST PARAMETERS
		username = request.POST["username"]
		fname = request.POST["fname"]
		lname = request.POST["lname"]
		email = request.POST["email"]
		pass1 = request.POST["pass1"]
		pass2 = request.POST["pass2"]

		# CHECK FOR ERRORNEOUS INPUTS
		if len(username) > 10:
			messages.error(request, "Username must be under 10 characters")
			return redirect("/")
		if not username.isalnum():
			messages.error(request, "Username should only contain letters & numbers")
		if pass1 != pass2:
			messages.error(request, "Passwords do not match")
			return redirect("/")
		
		# CREATE THE USER
		myuser = User.objects.create_user(username, email, pass1)
		myuser.first_name = fname
		myuser.last_name = lname
		myuser.save()
		messages.success(request, "Your iCoder account has been successfully created.")
		return redirect("/")
	else:
		return HttpResponse("404 - Not Found")

def handleLogin(request):
	if request.method == "POST":
		loginusername = request.POST["loginusername"]
		loginpass = request.POST["loginpass"]
		user = authenticate(username=loginusername, password=loginpass)
		if user is not None:
			login(request, user)
			messages.success(request, "Successfully Logged In.")
			return redirect("/")
		else:
			messages.error(request, "Invalid Credentials, please try again.")
			return redirect("/")
	return HttpResponse("404 - Not Found")

def handleLogout(request):
	logout(request)
	messages.success(request, "Successfully Logged Out.")
	return redirect("/")