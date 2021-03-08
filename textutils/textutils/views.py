# I HAVE CREATED THIS FILE - AARYAN

from django.http import HttpResponse
from django.shortcuts import render

def index(request):
	# return HttpResponse("<h1>HOME</h1>")
	# params = {"name": "Aaryan", "place": "Mars"}
	# return render(request, "index.html", params)
	return render(request, "index.html")

""" def about(request):
	return HttpResponse("ABOUT") """

def removepunc(request):
	# GET THE TEXT
	djtext = request.GET.get("text", "default")
	print(djtext)
	# ANALYZE THE TEXT
	return HttpResponse("remove punc")

def capfirst(request):
	return HttpResponse("capitalize first")

def newlineremove(request):
	return HttpResponse("newline remove")

def spaceremove(request):
	return HttpResponse("space remover")

def charcount(request):
	return HttpResponse("charcount")