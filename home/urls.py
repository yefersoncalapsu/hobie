from django .urls import path
from django.contrib import admin
from .views import*



urlpatterns = [
	#-----------------------------------------------------------------------------
	##listado de consultas bd
	path('lista_producto/', vista_lista_producto, name='producto'),
	path('lista_categoria/', vista_categoria, name='categoria'),
	path('lista_marca/', vista_marca, name='marca'),
	#------------------------------------------------------------------------------
	# url de template para funcion de agregar
	path('agregar/', vista_agregar, name='agregar'),
	#------------------------------------------------------------------------------
	# url de procedimiento de agregar para cada tabla
	path('agregar_producto/',vista_agregar_producto, name='vista_agregar_producto'),
	path('agregar_categoria/',vista_agregar_categoria, name='vista_agregar_categoria'),
	path('agregar_marca/',vista_agregar_marca, name='vista_agregar_marca'),
	
	#------------------------------------------------------------------------------
	##detalle de cada dato de una tabla
	path('ver_producto/<int:id_prod>/', vista_ver_producto, name='ver_producto'),
	path('ver_categoria/<int:id_catg>/', vista_ver_categoria, name='ver_categoria'),
	path('ver_marca/<int:id_marc>/', vista_ver_marca, name='ver_marca'),

	##-----------------------------------------------------------------------------
	# urls de procedimiento de editar datos de una tabla
	path('editar_producto/<int:id_prod>/', vista_editar_producto, name='editar_producto'),
	path('editar_categoria/<int:id_catg>/', vista_editar_categoria, name='editar_categoria'),
	path('editar_marca/<int:id_marc>/', vista_editar_marca, name='editar_marca'),

	##-----------------------------------------------------------------------------
	# urls de procedimiento de eliminar datos de una tabla
	path('eliminar_producto/<int:id_prod>/', vista_eliminar_producto,name='eliminar_producto'),
	path('eliminar_categoria/<int:id_catg>/', vista_eliminar_categoria,name='eliminar_categoria'),
	path('eliminar_marca/<int:id_marc>/', vista_eliminar_marca,name='eliminar_marca'),

	#------------------------------------------------------------------------------
	##detalle de cada dato de una tabla
	path('ver_producto/<int:id_prod>/', vista_ver_producto, name='ver_producto'),
	path('ver_categoria/<int:id_catg>/', vista_ver_categoria, name='ver_categoria'),
	path('ver_marca/<int:id_marc>/', vista_ver_marca, name='ver_marca'),

	#----------------------------------------------
	# url de login o inicio de sesion
	path('login/', vista_login, name='login'),

	#----------------------------------------------
	# url de log out o cierre de sesion
	path('logout/', vista_logout, name='logout'),
	
	#----------------------------------------------
	# url para el registr de un usuario
	path('register/', vista_register, name='registrar'),

	#--------------------------------------------------------------
	##servisios web
	path('wsxml/productos', ws_productos_vistaxml, name = 'xml'),
	path('wsjson/productos', ws_productos_vistajson, name = 'json'),
	#--------------------------------------------------------------
	# url de templates bases
	path('base1/', vista_base1, name='base1'),
	path('base2/', vista_base2, name='base2'),

	#----------------------------------------------
	# url de templates de inicio en la base1 y base2
	path('', vista_inicio_base1, name='inicio1'),
	path('inicio2/', vista_inicio_base2, name='inicio2'),
	

]