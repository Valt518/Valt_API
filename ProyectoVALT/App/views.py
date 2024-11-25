from django.shortcuts import render,get_object_or_404
from App.models import *
from .forms import crear_Usuarios_forms, crear_Empleados_forms, crear_Productos_forms, crear_Compra_detalle_forms, crear_Venta_detalle_forms,UserRegisterForm
from django.contrib import messages
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.forms import AuthenticationForm
# Create your views here.

def mostrar_index(request):
    
    
    return render(request, 'App/index.html')


def mostrar_usuarios(request):
    
    usuarios = Usuarios.objects.all()
    
    context ={'usuarios': usuarios}
    
    return render(request, 'App/usuarios.html', context=context)

def mostrar_productos(request):
    
    productos = Productos.objects.all()
    
    context = {'productos': productos}

    return render(request, 'App/productos.html', context=context)

def mostrar_empleados(request):
    
    empleados = Empleados.objects.all()
    
    context = {'empleados': empleados}
    
    return render(request, 'App/empleados.html', context=context)

def mostrar_venta_detalles(request):
    venta_detalle = Venta_detalles.objects.all()
    
    context = {'venta_detalle':  venta_detalle}
    
    return render(request, 'App/venta_detalle.html', context=context)


def mostrar_compra_detalles(request):
    compra_detalle = Compra_detalles.objects.all()
    
    context = {'compra_detalle': compra_detalle}
    
    return render(request, 'App/compra_detalle.html', context=context)



def crear_usuarios(request):
    if request.method == 'POST':
        form = crear_Usuarios_forms(request.POST)
        
        if form.is_valid():
            
            formulario_limpio = form.cleaned_data
            
            usuarios = Usuarios(nombre_usuario = formulario_limpio['nombre_usuario'],email_usuario = formulario_limpio['email_usuario'],telefono_usuario = formulario_limpio['telefono_usuario'],localidad_usuario = formulario_limpio['localidad_usuario'])
            
            usuarios.save()
            
            return render(request, 'App/index.html')
    else:
        form = crear_Usuarios_forms
        return render (request, 'App/crear_usuarios.html', {'form': crear_Usuarios_forms})

def crear_empleados(request):
    if request.method == 'POST':
        form = crear_Empleados_forms(request.POST)
        
        if form.is_valid():
            
            formulario_limpio = form.cleaned_data
            
            usuarios = Empleados(nombre_empleado = formulario_limpio['nombre_empleado'],email_empleado = formulario_limpio['email_empleado'],telefono_empleado = formulario_limpio['telefono_empleado'])
            
            usuarios.save()
            
            return render(request, 'App/index.html')
    else:
        form = crear_Empleados_forms()
        return render (request, 'App/crear_empleados.html', {'form': crear_Empleados_forms})

def crear_productos(request):
    if request.method == 'POST':
        form = crear_Productos_forms(request.POST)
        
        if form.is_valid():
            formulario_limpio = form.cleaned_data
            productos = Productos(nombre_producto = formulario_limpio['nombre_producto'],marca_producto= formulario_limpio['marca_producto'],precio_producto = formulario_limpio['precio_producto'],categoria_producto = formulario_limpio['categoria_producto'])
            productos.save()
            return render(request, 'App/index.html')
    else:
        form = crear_Productos_forms()
        return render(request, 'App/crear_productos.html', {'form': crear_Productos_forms})

def crear_compra_detalle(request):
    if request.method == 'POST':
        form = crear_Compra_detalle_forms(request.POST)
        if form.is_valid():
            formulario_limpio = form.cleaned_data
            compra_detalle = Compra_detalles(monto = formulario_limpio['monto'], fecha = formulario_limpio['fecha'], forma_de_pago = formulario_limpio['forma_de_pago'], producto = formulario_limpio['producto'])
            compra_detalle.save()
            return render (request, 'App/accion_compra.html')
    else:
        form = crear_Compra_detalle_forms()
        return render (request, 'App/crear_compra_detalles.html', {'form': crear_Compra_detalle_forms})


def crear_venta_detalle(request):
    if request.method == 'POST':
        form = crear_Venta_detalle_forms(request.POST)
        if form.is_valid():
            formulario_limpio = form.cleaned_data
            venta_detalle = Venta_detalles(monto = formulario_limpio['monto'], fecha=formulario_limpio['fecha'], forma_de_pago = formulario_limpio['forma_de_pago'], producto = formulario_limpio['producto'], usuario = formulario_limpio['usuario'])
            venta_detalle.save()
            return render (request, 'App/index.html')
    else:
        form = crear_Venta_detalle_forms()
        return render (request, 'App/crear_venta_detalles.html', {'form': crear_Venta_detalle_forms})


######## VSITAS PARA EL METODO CRUD 'READ'


def buscar_usuarios(request):
    if request.GET.get('email_usuario', False):
        email_usuario = request.GET['email_usuario']
        usuario = Usuarios.objects.filter(email_usuario__icontains=email_usuario)
        return render(request, 'App/buscar_usuario.html', {'usuario':usuario})
    else:
        respuesta = 'NO HAY DATOS'
    return render (request, 'App/buscar_usuario.html', {'respuesta': respuesta})

def buscar_empleados(request):
    if request.GET.get('nombre_empleado', False):
        nombre_empleado = request.GET['nombre_empleado']
        empleado = Empleados.objects.filter(nombre_empleado__icontains = nombre_empleado)
        return render (request, 'App/buscar_empleado.html', {'empleado':empleado})
    else:
        respuesta = 'NO HAY DATOS'
        return render (request, 'App/buscar_empleado.html', {'respuesta':respuesta})

def buscar_productos(request):
    if request.GET.get('nombre_producto', False):
        nombre_producto = request.GET['nombre_producto']
        producto = Productos.objects.filter(nombre_producto__icontains = nombre_producto)
        return render (request, 'App/buscar_producto.html', {'producto':producto})
    else:
        respuesta = 'NO HAY DATOS'
        return render (request, 'App/buscar_producto.html', {'respuesta':respuesta})

def buscar_compra_detalle(request):
    if request.GET.get('forma_de_pago', False):
        forma_de_pago = request.GET['forma_de_pago']
        compra_detalle = Compra_detalles.objects.filter(forma_de_pago__icontains = forma_de_pago)
        return render (request, 'App/buscar_compra_detalle.html', {'compra_detalle':compra_detalle})
    else:
        respuesta = 'NO HAY DATOS'
        return render (request, 'App/buscar_compra_detalle.html', {'respuesta':respuesta})

def buscar_venta_detalle(request):
    if request.GET.get('forma_de_pago', False):
        forma_de_pago = request.GET['forma_de_pago']
        venta_detalle = Venta_detalles.objects.filter(forma_de_pago__icontains = forma_de_pago)
        return render (request, 'App/buscar_venta_detalle.html', {'venta_detalle': venta_detalle})
    else:
        respuesta = 'NO HAY DATOS'
        return render (request, 'App/buscar_venta_detalle.html', {'respuesta':respuesta})

## DELETE PARA CRUD ↓

def eliminar_usuario(request,usuarios_id):
    usuarios = Usuarios.objects.get(id=usuarios_id)
    usuarios.delete()
    usuario = usuarios.objects.all()
    context = {'usuario' : usuario}
    return render(request, 'App/index.html', context=context)

def eliminar_productos(request,productos_id):
    productos = Productos.objects.get(id=productos_id)
    productos.delete()
    producto = productos.objects.all()
    context = {'producto' : producto}
    return render(request, 'App/index.html', context=context)

def eliminar_empleados(request,empleados_id):
    empleados = Empleados.objects.get(id=empleados_id)
    empleados.delete()
    empleado = empleados.objects.all()
    context = {'empleado' : empleado}
    return render(request, 'App/index.html', context=context)

def eliminar_venta_detalle (request,venta_detalle_id):
    venta_detalles = Venta_detalles.objects.get(id=venta_detalle_id)
    venta_detalles.delete()
    venta_detalle = venta_detalles.objects.all()
    context = {'venta_detalle' : venta_detalle}
    return render(request, 'App/index.html', context=context)

def eliminar_compra_detalle(request,compra_detalle_id):
    compra_detalles = Compra_detalles.objects.get(id=compra_detalle_id)
    compra_detalles.delete()
    compra_detalle = compra_detalles.objects.all()
    context = {'compra_detalle' : compra_detalle}
    return render(request, 'App/index.html', context=context)

## UPDATE PARA CRUD ↓

def actualizar_productos(request,productos_id):
    productos = Productos.objects.get(id=productos_id)
    if request.method == 'POST':
        form = crear_Productos_forms(request.POST)

        if form.is_valid():

            formulario_limpio = form.cleaned_data

            productos.nombre_producto = formulario_limpio['nombre_producto']
            productos.marca_producto = formulario_limpio['marca_producto']
            productos.precio_producto =  formulario_limpio['precio_producto']
            productos.categoria_producto= formulario_limpio['categoria_producto']
            productos.save()

            return render(request, 'App/index.html')

    else:
        form = crear_Productos_forms(initial={'nombre_producto': productos.nombre_producto, 'marca_producto': productos.marca_producto,'precio_producto': productos.precio_producto,'categoria_producto': productos.categoria_producto })
        
    return render(request, 'App/actualizar_producto.html', {'form': crear_Productos_forms})


def actualizar_usuarios(request,usuarios_id):
    usuarios = Usuarios.objects.get(id=usuarios_id)
    if request.method == 'POST':
        form = crear_Usuarios_forms(request.POST)

        if form.is_valid():

            formulario_limpio = form.cleaned_data

            usuarios.nombre_usuario = formulario_limpio['nombre_usuario']
            usuarios.email_usuario = formulario_limpio['email_usuario']
            usuarios.telefono_usuario  = formulario_limpio['telefono_usuario']
            usuarios.localidad_usuario = formulario_limpio['localidad_usuario']
            usuarios.save()

            return render(request, 'App/index.html')

    else:
        form = crear_Usuarios_forms(initial={'nombre_producto': usuarios.nombre_usuario, 'email_usuario': usuarios.email_usuario,'telefono_usuario': usuarios.telefono_usuario,'localidad_usuario': usuarios.localidad_usuario })
        
    return render(request, 'App/actualizar_usuario.html', {'form': crear_Usuarios_forms})


def actualizar_empleados(request,empleados_id):
    empleados = Empleados.objects.get(id=empleados_id)
    if request.method == 'POST':
        form = crear_Empleados_forms(request.POST)

        if form.is_valid():

            formulario_limpio = form.cleaned_data

            empleados.nombre_empleado = formulario_limpio['nombre_empleado']
            empleados.email_empleado = formulario_limpio['email_empleado']
            empleados.telefono_empleado = formulario_limpio['telefono_empleado']
            empleados.save()

            return render(request, 'App/index.html')

    else:
        form = crear_Empleados_forms(initial={'nombre_empleado': empleados.nombre_empleado, 'email_usuario': empleados.email_empleado,'telefono_usuario': empleados.telefono_empleado})
        
    return render(request, 'App/actualizar_empleado.html', {'form': crear_Empleados_forms})



def actualizar_compra_detalle(request,compra_detalle_id):
    compra_detalle = get_object_or_404(Compra_detalles, id=compra_detalle_id)
    if request.method == 'POST':
        form = crear_Compra_detalle_forms(request.POST)
        if form.is_valid():
            formulario_limpio = form.cleaned_data
            compra_detalle.monto = formulario_limpio['monto']
            compra_detalle.fecha = formulario_limpio['fecha']
            compra_detalle.forma_de_pago = formulario_limpio['forma_de_pago']
            compra_detalle.producto = formulario_limpio['producto']
            compra_detalle.save()
            return render(request, 'App/index.html')
    else:
            form = crear_Compra_detalle_forms(initial={'monto': compra_detalle.monto, 'fecha': compra_detalle.fecha,'forma_de_pago': compra_detalle.forma_de_pago,'producto': compra_detalle.producto })
    return render(request, 'App/actualizar_compra_detalle.html', {'form': crear_Compra_detalle_forms})


def actualizar_venta_detalle(request,venta_detalle_id):
    venta_detalle = Venta_detalles.objects.get(id=venta_detalle_id)
    if request.method == 'POST':
        form = crear_Venta_detalle_forms(request.POST)

        if form.is_valid():

            formulario_limpio = form.cleaned_data

            venta_detalle.monto = formulario_limpio['monto']
            venta_detalle.fecha = formulario_limpio['fecha']
            venta_detalle.forma_de_pago = formulario_limpio['forma_de_pago']
            venta_detalle.producto = formulario_limpio['producto']
            venta_detalle.usuario = formulario_limpio['usuario']
            venta_detalle.save()

            return render(request, 'App/index.html')

    else:
        form = crear_Venta_detalle_forms(initial={'monto': venta_detalle.monto, 'fecha': venta_detalle.fecha,'forma_de_pago': venta_detalle.forma_de_pago,'producto': venta_detalle.producto,'usuario': venta_detalle.usuario })
        
    return render(request, 'App/actualizar_venta_detalle.html', {'form': crear_Venta_detalle_forms})



#####VISTAS DE REGISTRO Y LOGIN
def registro_usuario(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, '¡Registro exitoso! Bienvenido/a.')
            return render (request, 'App/index.html')
    else:
            form = UserRegisterForm()

    return render(request, 'App/registro.html', {'form': form})

def login_request(request):
    if request.method == 'POST':
            form = AuthenticationForm(request, data = request.POST)
            if form.is_valid():
                usuario = form.cleaned_data.get('username')
                contraseña = form.cleaned_data.get('password')
                user = authenticate(username=usuario, password=contraseña)
            
                if user is not None:
                    login(request, user)
                    return render(request,'App/index.html', {'mensaje': f'bienvenido {usuario}!'})
                else:
                    return render(request,'App/index.html', {'mensaje': 'datos incorrectos.'})
            else:
                return render(request,'App/index.html', {'mensaje': 'formulario erroneo.'})
    form = AuthenticationForm()
    return render(request,'App/login.html', {'form':form})

def logout_request(request):
    logout(request)
    return render(request, 'App/index.html', {'mensaje': 'has cerrado sesiòn con exito.'})