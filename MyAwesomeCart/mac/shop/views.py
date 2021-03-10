from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
	# return HttpResponse("Index Shop")
	return render(request, "shop/index.html")

def about(request):
	return HttpResponse("About")
	# return render(request, "shop/index.html")

def contact(request):
	return HttpResponse("Contact")
	# return render(request, "shop/index.html")

def tracker(request):
	return HttpResponse("Tracker")
	# return render(request, "shop/index.html")

def search(request):
	return HttpResponse("Search")
	# return render(request, "shop/index.html")

def productView(request):
	return HttpResponse("Product View")
	# return render(request, "shop/index.html")

def checkout(request):
	return HttpResponse("Checkout")
	# return render(request, "shop/index.html")