from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms.widgets import PasswordInput, TextInput
from django.contrib.auth.forms import AuthenticationForm

class crear_Usuarios_forms(forms.Form):
    nombre_usuario = forms.CharField(max_length=30)
    email_usuario = forms.EmailField()
    telefono_usuario = forms.FloatField()
    localidad_usuario = forms.CharField(max_length=30)

class crear_Empleados_forms(forms.Form):
    nombre_empleado = forms.CharField(max_length=30)
    email_empleado = forms.EmailField()
    telefono_empleado = forms.FloatField()

class crear_Productos_forms(forms.Form):
    nombre_producto = forms.CharField(max_length=30)
    marca_producto = forms.CharField(max_length=30)
    precio_producto = forms.FloatField()
    categoria_producto = forms.CharField(max_length=30)

class crear_Compra_detalle_forms(forms.Form):
    monto = forms.FloatField()
    fecha = forms.DateField()
    forma_de_pago = forms.CharField(max_length=25)
    producto = forms.ModelChoiceField(queryset=Productos.objects.all())

class crear_Venta_detalle_forms(forms.Form):
    monto = forms.FloatField()
    fecha = forms.DateField()
    forma_de_pago = forms.CharField(max_length=25)
    producto = forms.ModelChoiceField(queryset=Productos.objects.all())
    usuario = forms.ModelChoiceField(queryset=Usuarios.objects.all())

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    password1 = forms.CharField(label='Contraseña',widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repetir contraseña',widget=forms.PasswordInput)
    
    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'password1',
            'password2',
        ]
        help_texts = {k: '' for k in fields}

class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=TextInput())
    password = forms.CharField(widget=PasswordInput())