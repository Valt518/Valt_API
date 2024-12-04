from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(Usuarios)
admin.site.register(Productos)
admin.site.register(Empleados)
admin.site.register(Venta_detalles)
admin.site.register(Compra_detalles)