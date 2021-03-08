# I HAVE CREATED THIS FILE - AARYAN

from django.http import HttpResponse

def index(request):
	return HttpResponse("<h1>HELLO</h1>")

def about(request):
	return HttpResponse("ABOUT")