#encoding:utf-8
from django.forms import ModelForm 
from django import forms 
from principal.models import Cuenta,Periodo,Transaccion,Movimiento,CierreApertura
from django.contrib.auth.models import User

class UserForm(ModelForm):
	class Meta:
		model=User

class PeriodoForm(ModelForm):
	class Meta:
		model=Periodo

class TransaccionForm(ModelForm):
	class Meta:
		model=Transaccion

class MovimientoForm(ModelForm):
	class Meta:
		model=Movimiento

class CuentaForm(ModelForm):
	class Meta:
		model=Cuenta

class CierreApertura(ModelForm):
	class Meta:
		model=CierreApertura

	