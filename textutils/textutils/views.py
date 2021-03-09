# I HAVE CREATED THIS FILE - AARYAN

from django.http import HttpResponse
from django.shortcuts import render

def index(request):
	# return HttpResponse("<h1>HOME</h1>")
	# params = {"name": "Aaryan", "place": "Mars"}
	# return render(request, "index.html", params)
	return render(request, "index.html")

def analyze(request):
	# GET THE TEXT
	djtext = request.GET.get("text", "default")

	# CHECK CHECKBOX VALUE
	removepunc = request.GET.get("removepunc", "off")
	fullcaps = request.GET.get("fullcaps", "off")
	newlineremover = request.GET.get("newlineremover", "off")
	extraspaceremover = request.GET.get("extraspaceremover", "off")
	
	# CHECK WHICH CHECKBOX IS ON
	if removepunc == "on":
		punctuations = '''!"#$%&'()*+, -./:;<=>?@[\]^_`{|}~'''
		analyzed = ""
		for char in djtext:
			if char not in punctuations:
				analyzed = analyzed + char
		params = {"purpose": "removed punctuations", "analyzed_text": analyzed}
		return render(request, "analyze.html", params)

	elif (fullcaps == "on"):
		analyzed = ""
		for char in djtext:
			analyzed = analyzed + char.upper()
		params = {"purpose": "changed to uppercase", "analyzed_text": analyzed}
		return render(request, "analyze.html", params)

	elif (newlineremover == "on"):
		analyzed = ""
		for char in djtext:
			if char != "\n":
				analyzed = analyzed + char
		params = {"purpose": "removed new lines", "analyzed_text": analyzed}
		return render(request, "analyze.html", params)

	elif (extraspaceremover == "on"):
		analyzed = ""
		for index, char in enumerate(djtext):
			if not(djtext[index] == " " and djtext[index + 1] == " "):
				analyzed = analyzed + char
		params = {"purpose": "removed new lines", "analyzed_text": analyzed}
		return render(request, "analyze.html", params)

	else:
		return HttpResponse("ERROR")