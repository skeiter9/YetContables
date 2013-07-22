from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User

def inicio(request):
	if not request.user.is_anonymous():
		return HttpResponseRedirect('/home')
	if request.method == 'POST':
		formulario = AuthenticationForm(request.POST)
		if formulario.is_valid :
			usuario=request.POST['username']			
			contrasena=request.POST['password']
			user = authenticate(username=usuario, password=contrasena)
			if user is not None:
				if user.is_active:
					login(request,user)
					return HttpResponseRedirect('/home')
				else :
					return render_to_response('no-activo.html', context_instance=RequestContext(request))
			else :
				return render_to_response('no-usuario.html', context_instance=RequestContext(request))
		else :
			return render_to_response('formulario-no-valido.html', context_instance=RequestContext(request))
	else:
		formulario= AuthenticationForm()
		return render_to_response('login.html',{'formulario':formulario} , context_instance=RequestContext(request))

@login_required(login_url="/")
def home(request) :
	usuario=request.user
	return render_to_response('home.html',{'usuario':usuario} , context_instance=RequestContext(request))

#Usuarios
@login_required(login_url="/")
def usuarios (request) :
	usuarios=User.objects.all()
	return render_to_response('usuarios.html',{'usuarios':usuarios} , context_instance=RequestContext(request))

@login_required(login_url="/")
def cerrar(request) :
	logout(request)
	return HttpResponseRedirect('/')

