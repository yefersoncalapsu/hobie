from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.core import serializers
from .models import*
from .forms import*



def vista_lista_producto(request):
	lista= Producto.objects.filter()
	return render(request, 'lista_producto.html', locals())

def vista_categoria(request):
	lista2= Categoria.objects.filter()
	return render(request, 'lista_categoria.html', locals())


def vista_marca(request):
	lista3= Marca.objects.filter()
	return render(request, 'lista_marca.html', locals())

def vista_agregar(request):
	return render(request, 'agregar.html', locals())


def vista_agregar_producto(request):
	if request.method == 'POST':
		formulario = agregar_producto_form(request.POST,request.FILES)
		if formulario.is_valid():
			prod = formulario.save(commit =False)
			prod.status = True
			prod.save()
			formulario.save_m2m()
			return redirect ('/lista_producto/')
	else:
		formulario=agregar_producto_form()
	return render(request, 'vista_agregar_producto.html', locals())

def vista_agregar_categoria(request):
	if request.method == 'POST':
		formulario = agregar_categoria_form(request.POST,request.FILES)
		if formulario.is_valid():
			catg = formulario.save(commit =False)
			catg.save()
			formulario.save_m2m()
			return redirect ('/lista_categoria/')
	else:
		formulario=agregar_categoria_form()
	return render(request, 'vista_agregar_categoria.html', locals())

def vista_agregar_marca(request):
	if request.method == 'POST':
		formulario = agregar_marca_form(request.POST,request.FILES)
		if formulario.is_valid():
			marc = formulario.save(commit =False)
			marc.save()
			formulario.save_m2m()
			return redirect ('/lista_marca/')
	else:
		formulario=agregar_producto_form()
	return render(request, 'vista_agregar_marca.html', locals())
	
def vista_editar_producto(request, id_prod):
	prod= Producto.objects.get(id=id_prod)
	if request.method == "POST":
		formulario = agregar_producto_form(request.POST)
		if formulario.is_valid():
			prod = formulario.save()
			return redirect ('/lista_producto/')
	else:
		formulario = agregar_producto_form(instance=prod)
	return render(request, 'vista_agregar_producto.html', locals())

def vista_editar_categoria(request, id_catg):
	catg= Categoria.objects.get(id=id_catg)
	if request.method == "POST":
		formulario = agregar_categoria_form(request.POST)
		if formulario.is_valid():
			catg = formulario.save()
			return redirect ('/lista_categoria/')
	else:
		formulario = agregar_categoria_form(instance=catg)
	return render(request, 'vista_agregar_categoria.html', locals())

def vista_editar_marca(request, id_marc):
	marc= Marca.objects.get(id=id_marc)
	if request.method == "POST":
		formulario = agregar_marca_form(request.POST)
		if formulario.is_valid():
			prod = formulario.save()
			return redirect ('/lista_marca/')
	else:
		formulario = agregar_marca_form(instance=marc)
	return render(request, 'vista_agregar_marca.html', locals())

def vista_eliminar_producto(request, id_prod):
	prod = Producto.objects.get(id=id_prod)
	prod.delete()
	return redirect('/lista_producto/')

def vista_eliminar_categoria(request, id_catg):
	catg = Categoria.objects.get(id=id_catg)
	catg.delete()
	return redirect('/lista_categoria/')

def vista_eliminar_marca(request, id_marc):
	marc = Marca.objects.get(id=id_marc)
	marc.delete()
	return redirect('/lista_marca/')


def vista_ver_producto(request, id_prod):
	p = Producto.objects.get(id=id_prod)
	return render(request,'ver_producto.html',locals())

def vista_ver_categoria(request, id_catg):
	c = Categoria.objects.get(id=id_catg)
	return render(request,'ver_categoria.html',locals())

def vista_ver_marca(request, id_marc):
	m = Marca.objects.get(id=id_marc)
	return render(request,'ver_marca.html',locals())


def vista_login (request):
	usu = ""
	cla = ""
	if request.method == "POST":
		formulario = login_form(request.POST)
		if formulario.is_valid():
			usu = formulario.cleaned_data['usuario']
			cla = formulario.cleaned_data['clave']
			usuario = authenticate(username=usu, password=cla)
			if usuario is not None and usuario.is_active:
				login(request, usuario)
				return redirect('/inicio2/')
			else:
				msj = "usuario o clave incorrectos "
	formulario = login_form()
	return render(request, 'login.html', locals())

def vista_logout (request):
	logout(request)
	return redirect('/login/')



def vista_register(request):
	formulario = register_form()
	if request.method == 'POST':
		formulario = register_form(request.POST)
		if formulario.is_valid():
			usuario = formulario.cleaned_data['username']
			correo 	= formulario.cleaned_data['email']
			password_1 = formulario.cleaned_data['password_1']
			password_2 = formulario.cleaned_data['password_2']
			u = User.objects.create_user(username=usuario, email=correo, password=password_1)
			u.save()
			return render(request, 'gracias_por_registrarse.html', locals())
		else:
			return render(request, 'register.html', locals())
	return render(request, 'register.html', locals())

##---------------------------------------------
## vista para ver el ws en formato xml
def ws_productos_vistaxml(request):
	data = serializers.serialize('xml', Producto.objects.filter(status=True))
	return HttpResponse(data, content_type='application/xml')

##---------------------------------------------
## vista para ver el ws en formato json
def ws_productos_vistajson(request):
	data = serializers.serialize('json', Producto.objects.filter(status=True))
	return HttpResponse(data, content_type='application/json')

## ---------------------------------------------
##base1 para los templates de register y login
def vista_base1(request):
	return render(request, 'base.html', locals())
##----------------------------------------------
## base2 para los demas templates depues de
## iniciar sesion
def vista_base2(request):
	User.objects.filter()
	return render(request, 'base2.html', locals())

##----------------------------------------------
## template que inicia al ejecutar el puerto
## 127.0.0.1:8000
def vista_inicio_base1(request):
	return render(request, 'inicio1.html', locals())

##-----------------------------------------------
## template al cual es redirigido despues
# de haber iniciado sesion
def vista_inicio_base2(request):
	return render(request, 'inicio2.html', locals())