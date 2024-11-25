from django.contrib import admin
from django.urls import path
from App import views
urlpatterns = [
###URLS DE LOS MODELS DE LA API
    path('', views.mostrar_index, name='INDEX'),
    path('compra_detalle/', views.mostrar_compra_detalles, name='COMPRA'),
    path('empleados/', views.mostrar_empleados, name='EMPLEADOS'),
    path('productos/', views.mostrar_productos, name='PRODUCTOS'),
    path('usuarios/', views.mostrar_usuarios, name='USUARIOS'),
    path('venta_detalle/', views.mostrar_venta_detalles, name='VENTAS'),
###URLS DE CREAR VENTA DETALLES
    path('crear_venta_detalle/', views.crear_venta_detalle, name='CREAR_VENTAS_DETALLES'),
    path('crear_compra_detalle/', views.crear_compra_detalle, name='CREAR_COMPRA_DETALLES'),
    path('crear_producto/', views.crear_productos, name='CREAR_PRODUCTOS'),
    path('crear_empleados/', views.crear_empleados, name='CREAR_EMPLEADOS'),
    path('crear_usuarios/', views.crear_usuarios, name='CREAR_USUARIOS'),
###URLS DE BUSCAR DETALLE
    path('buscar_venta_detalle/', views.buscar_venta_detalle, name='BUSCAR_VENTAS_DETALLE'),
    path('buscar_compra_detalle/', views.buscar_compra_detalle, name='BUSCAR_COMPRA_DETALLE'),
    path('buscar_producto/', views.buscar_productos, name='BUSCAR_PRODUCTOS'),
    path('buscar_empleados/', views.buscar_empleados, name='BUSCAR_EMPLEADOS'),
    path('buscar_usuarios/', views.buscar_usuarios, name='BUSCAR_USUARIOS'),
###URLS DE ACTUALIZAR
    path('actualizar_venta_detalle/<venta_detalle_id>/', views.actualizar_venta_detalle, name='ACTUALIZAR_VENTA_DETALLE'),
    path('actualizar_compra_detalle/<compra_detalle_id>/', views.actualizar_compra_detalle, name='ACTUALIZAR_COMPRA_DETALLE'),
    path('actualizar_producto/<productos_id>/', views.actualizar_productos, name='ACTUALIZAR_PRODUCTO'),
    path('actualizar_usuario/<usuarios_id>/', views.actualizar_usuarios, name='ACTUALIZAR_USUARIO'),
    path('actualizar_empleado/<empleados_id>/', views.actualizar_empleados, name='ACTUALIZAR_EMPLEADO'),
###URLS DE ELIMINAR
    path('eliminar_venta_detalle/<venta_detalle_id>/', views.eliminar_venta_detalle, name='ELIMINAR_VENTA_DETALLE'),
    path('eliminar_compra_detalle/<compra_detalle_id>/', views.eliminar_compra_detalle, name='ELIMINAR_COMPRA_DETALLE'),
    path('eliminar_empleado/<empleados_id>/', views.eliminar_empleados, name='ELIMINAR_EMPLEADOS'),
    path('eliminar_producto/<productos_id>/', views.eliminar_productos, name='ELIMINAR_PRODUCTOS'),
    path('eliminar_usuario/<usuarios_id>/', views.eliminar_usuario, name='ELIMINAR_USUARIOS'),
    path('registro/', views.registro_usuario,name='REGISTRO'),
    path('login/', views.login_request, name = 'LOGIN'),
    path('logout/', views.logout_request, name = 'LOGOUT')
]
