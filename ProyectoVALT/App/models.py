from django.db import models

# Create your models here.

class Usuarios (models.Model):
    nombre_usuario = models.CharField(max_length=30)
    email_usuario = models.EmailField()
    telefono_usuario = models.IntegerField()
    localidad_usuario = models.CharField(max_length=30)

    def __str__ (self):
        return f'Nombre_usuario: {self.nombre_usuario}, Email : {self.email_usuario}, telefono : {self.telefono_usuario}, localidad : {self.localidad_usuario}'

class Productos (models.Model):
    nombre_producto = models.CharField(max_length=30)
    marca_producto = models.CharField(max_length=30)
    precio_producto = models.FloatField()
    categoria_producto = models.CharField(max_length=30)

    def __str__(self):
        return f'Nombre_producto: {self.nombre_producto}, Marca : {self.marca_producto}, Precio {self.precio_producto}, Categoria {self.categoria_producto}'

class Empleados (models.Model):
    nombre_empleado = models.CharField(max_length=30)
    email_empleado = models.EmailField()
    telefono_empleado = models.IntegerField()

    def __str__ (self):
        return f'Nombre_usuario: {self.nombre_empleado}, Email : {self.email_empleado}, telefono : {self.telefono_empleado}'

class Venta_detalles (models.Model):
    monto = models.FloatField()
    fecha = models.DateField()
    forma_de_pago = models.CharField(max_length=25)
    producto = models.ForeignKey(Productos,on_delete=models.CASCADE)
    usuario = models.ForeignKey(Usuarios,on_delete=models.CASCADE)

    def __str__(self):
        return f'Monto: {self.monto}, Fecha : {self.fecha}, Forma_de_pago {self.forma_de_pago}, producto {self.producto}, usuario {self.usuario}'

class Compra_detalles (models.Model):
    monto = models.FloatField()
    fecha = models.DateField()
    forma_de_pago = models.CharField(max_length=25)
    producto = models.ForeignKey(Productos,on_delete=models.CASCADE)
    def __str__(self):
        return f'Monto: {self.monto}, Fecha : {self.fecha}, Forma_de_pago {self.forma_de_pago}, producto {self.producto}'