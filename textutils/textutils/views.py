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

""" def removepunc(request):
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
	return HttpResponse("charcount") """

def analyze(request):
	# GET THE TEXT
	djtext = request.GET.get("text", "default")
	removepunc = request.GET.get("removepunc", "off")
	print(djtext)
	print(removepunc)
	# analyzed = djtext
	if removepunc == "on":
		punctuations = '''!"#$%&'()*+, -./:;<=>?@[\]^_`{|}~'''
		analyzed = ""
		for char in djtext:
			if char not in punctuations:
				analyzed = analyzed + char
		params = {"purpose": "removed punctuations", "analyzed_text": analyzed}
		# ANALYZE THE TEXT
		# return HttpResponse("remove punc")
		# remove //!.. this
		return render(request, "analyze.html", params)
	else:
		return HttpResponse("ERROR")