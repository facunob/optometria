from django.contrib import admin
from .models import Paciente, Turno, HistorialMedico, Lente, Producto,Pedido



admin.site.register(Paciente)
admin.site.register(Turno)
admin.site.register(HistorialMedico)
admin.site.register(Lente)
admin.site.register(Producto)
admin.site.register(Pedido)