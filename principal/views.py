from django.contrib.auth.forms import AuthenticationForm,UserCreationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from principal.forms import CuentaForm,TransaccionForm,MovimientoForm,CuentaForm,CierreApertura,PeriodoForm,UserForm
from principal.models import Cuenta,Periodo,Transaccion,Movimiento,CierreApertura

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
	if request.method=='POST' :
		userForm=UserCreationForm(request.POST)
		if userForm.is_valid() :
			userForm.save()
			return HttpResponseRedirect('/usuarios')
	elif 'userSelect' in request.GET :
		usuario=request.user
		usuarios=User.objects.all()
		userForm=UserCreationForm()
		editUserForm=UserForm()
		userSelected=User.objects.get(pk=request.GET['userSelect'])
		return render_to_response('usuarios.html',{'editUserForm':editUserForm,'userSelected':userSelected,'usuario':usuario,'userForm':userForm,'usuarios':usuarios} , context_instance=RequestContext(request))
	
	else :
		usuario=request.user
		usuarios=User.objects.all()
		userForm=UserCreationForm()
		userSelected=""
		return render_to_response('usuarios.html',{'userSelected':userSelected,'usuario':usuario,'userForm':userForm,'usuarios':usuarios} , context_instance=RequestContext(request))

@login_required
def user_profile(request):
    success = False
    user = User.objects.get(pk=request.user.id)
    if request.method == 'POST':
        upform = UserProfileForm(request.POST, instance=user.get_profile())
        if upform.is_valid():
            up = upform.save(commit=False)
            up.user = request.user
            up.save()
            success = True
    else:
        upform = UserProfileForm(instance=user.get_profile())       

    return render_to_response('upload-user.html',
        locals(), context_instance=RequestContext(request))

@login_required(login_url="/")
def cerrar(request) :
	logout(request)
	return HttpResponseRedirect('/')

@login_required(login_url="/")
def plan(request) :
	if request.method=='POST':
		cuentaForm=CuentaForm(request.POST)
		if cuentaForm.is_valid():
			cuentaForm.save()
			return HttpResponseRedirect('/home')
	else :
		usuario=request.user
		cuentaForm=CuentaForm()
		cuentas=Cuenta.objects.all
		return render_to_response('plan-contable.html',{'usuario':usuario,'cuentaForm':cuentaForm,'cuentas':cuentas}, context_instance=RequestContext(request) )
#periodo
@login_required(login_url="/")
def periodo(request) :
	usuario=request.user
	periodoForm=PeriodoForm()
	return render_to_response('periodo.html',{'usuario':usuario,'periodoForm':periodoForm}, context_instance=RequestContext(request) )
@login_required(login_url="/")
def transacciones(request) :
	usuario=request.user
	return render_to_response('transacciones.html',{'usuario':usuario}, context_instance=RequestContext(request) )
@login_required(login_url="/")
def libroDiario(request) :
	usuario=request.user
	return render_to_response('libro-diario.html',{'usuario':usuario}, context_instance=RequestContext(request) )
@login_required(login_url="/")
def libroMayor(request) :
	usuario=request.user
	return render_to_response('libro-mayor.html',{'usuario':usuario}, context_instance=RequestContext(request) )

#Cierre y apertura de cuentas 
@login_required(login_url="/")
def cierreYApertura(request) :
	usuario=request.user
	return render_to_response('cierre-y-apertura-de-cuentas.html',{'usuario':usuario}, context_instance=RequestContext(request) )


