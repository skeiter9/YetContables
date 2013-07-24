#coding:utf-8
from django.db import models
from django.contrib.auth.models import User

#Opcion menu
class OpcionMenu(models.Model):
	nombre= models.CharField(max_length=100,help_text='Opción menu')
	url= models.CharField(max_length=100)
	def __unicode__(self):
		return self.nombre

# Tipos de Usuario
class TipoUsuario(models.Model):
	nombre=models.CharField(max_length=100)
	descripcion=models.TextField(verbose_name='Descripción')
	def __unicode__(self):
		return self.nombre

#Asignacion de Menu según Tipo de Usuario
class AsignacionMenu(models.Model):
	opcionMenu= models.ForeignKey(OpcionMenu)
	tipoUsuario= models.ForeignKey(TipoUsuario)
	def __unicode__(self):
		return self.tipoUsuario

#Periodo
class Periodo(models.Model):
	fechaInicio=models.DateTimeField()
	fechaFin=models.DateTimeField()
	estado=models.CharField(max_length=2)
	cerrado=models.CharField(max_length=2)
	usuario=models.ForeignKey(User)
	def __unicode__(self):
		return unicode(self.fechaInicio)

#Transacción
class Transaccion(models.Model):
	numero=models.IntegerField()
	fecha=models.DateTimeField()
	nombre=models.CharField(max_length=100)
	montoTotal=models.DecimalField(max_digits=10,decimal_places=3)
	usuario=models.ForeignKey(User)
	periodo=models.ForeignKey(Periodo)
	def __unicode__(self):
		return self.nombre

#Movimientos
class Movimiento(models.Model):
	cuenta=models.CharField(max_length=20)
	monto=models.DecimalField(max_digits=10,decimal_places=3)
	tipo=models.CharField(max_length=2)
	transaccion=models.ForeignKey(Transaccion)
	def __unicode__(self):
		return self.cuenta

#Cuentas
class Cuenta(models.Model):
	nombre=models.CharField(max_length=100)
	numCuenta=models.IntegerField()
	cuentaOrigin=models.CharField(max_length=20)
	tipo=models.CharField(max_length=50)
	estado=models.CharField(max_length=2)
	def __unicode__(self):
		return unicode(self.nombre)

#Cierre Apertura
class CierreApertura(models.Model):
	cuenta=models.CharField(max_length=20)
	posicionInicial=models.CharField(max_length=2)
	posicionFinal=models.CharField(max_length=2)
	saldoInicial=models.DecimalField(max_digits=10,decimal_places=3)
	saldoFinal=models.DecimalField(max_digits=10,decimal_places=3)
	periodo=models.ForeignKey(Periodo)
	def __unicode__(self):
		return self.cuenta
