# I HAVE CREATED THIS FILE - AARYAN

from django.http import HttpResponse

def index(request):
	return HttpResponse("<h1>HOME</h1>")

""" def about(request):
	return HttpResponse("ABOUT") """

def removepunc(request):
	return HttpResponse("remove punc")

def capfirst(request):
	return HttpResponse("capitalize first")

def newlineremove(request):
	return HttpResponse("newline remove")

def spaceremove(request):
	return HttpResponse("space remover")

def charcount(request):
	return HttpResponse("charcount")