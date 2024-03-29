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
	# djtext = request.GET.get("text", "default")
	djtext = request.POST.get("text", "default")

	# CHECK CHECKBOX VALUE
	removepunc = request.POST.get("removepunc", "off")
	fullcaps = request.POST.get("fullcaps", "off")
	newlineremover = request.POST.get("newlineremover", "off")
	extraspaceremover = request.POST.get("extraspaceremover", "off")
	
	# CHECK WHICH CHECKBOX IS ON
	if removepunc == "on":
		punctuations = '''!"#$%&'()*+, -./:;<=>?@[\]^_`{|}~'''
		analyzed = ""
		for char in djtext:
			if char not in punctuations:
				analyzed = analyzed + char
		params = {"purpose": "removed punctuations", "analyzed_text": analyzed}
		djtext = analyzed
		# return render(request, "analyze.html", params)

	# elif (fullcaps == "on"):
	if (fullcaps == "on"):
		analyzed = ""
		for char in djtext:
			analyzed = analyzed + char.upper()
		params = {"purpose": "changed to uppercase", "analyzed_text": analyzed}
		djtext = analyzed
		# return render(request, "analyze.html", params)

	# elif (newlineremover == "on"):
	if (newlineremover == "on"):
		analyzed = ""
		for char in djtext:
			if char != "\n" and char != "\r":
				analyzed = analyzed + char
		params = {"purpose": "removed new lines", "analyzed_text": analyzed}
		djtext = analyzed
		# return render(request, "analyze.html", params)

	# elif (extraspaceremover == "on"):
	if (extraspaceremover == "on"):
		analyzed = ""
		for index, char in enumerate(djtext):
			if not(djtext[index] == " " and djtext[index + 1] == " "):
				analyzed = analyzed + char
		params = {"purpose": "removed new lines", "analyzed_text": analyzed}
		djtext = analyzed
		# return render(request, "analyze.html", params)

	# else:
	# 	return HttpResponse("ERROR")

	if ((removepunc != "on") and (fullcaps != "on") and (newlineremover != "on") and (extraspaceremover != "on")):
		return HttpResponse("ERROR")

	return render(request, "analyze.html", params)
