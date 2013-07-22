from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext

def home(request):
	html= "<h1>Prueba</h1>"
	return HttpResponse(html)

def login(request):
	return render_to_response('login.html', context_instance=RequestContext(request))
	