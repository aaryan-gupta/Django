from django.shortcuts import render
from django.http import HttpResponse
from .models import Product
from math import ceil

# Create your views here.

def index(request):
	# return HttpResponse("Index Shop")
	# products = Product.objects.all()
	# print(products)
	""" n = len(products)
	nSlides = n//4 + ceil((n/4) - (n//4)) """
	# params = {"no_of_slides": nSlides, "range": range(1, nSlides), "product": products}
	# allProds = [[products, range(1, nSlides), nSlides], [products, range(1, nSlides), nSlides]]
	allProds = []
	catProds = Product.objects.values("category", "id")
	cats = {item["category"] for item in catProds}
	for cat in cats:
		prod = Product.objects.filter(category=cat)
		n = len(prod)
		nSlides = n//4 + ceil((n/4) - (n//4))
		allProds.append([prod, range(1, nSlides), nSlides])
	params = {"allProds" : allProds}
	return render(request, "shop/index.html", params)

def about(request):
	# return HttpResponse("About")
	return render(request, "shop/about.html")

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