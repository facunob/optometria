from django.db import models
from usuario.models import Usuario

class Paciente(models.Model):
  nombre = models.CharField(max_length=50)
  apellido = models.CharField(max_length=50)
  dni = models.CharField(max_length=12)
  obra_social = models.CharField(max_length=30)

  def __str__(self):
    return f'Paciente:{self.nombre},{self.apellido}'


class Turno(models.Model):
  medico = models.ForeignKey(Usuario,on_delete=models.CASCADE)
  paciente = models.ForeignKey(Paciente,on_delete=models.CASCADE)
  fecha = models.DateTimeField()
  asistencia = models.BooleanField(default=False)

  def __str__(self):
    return f'Turno:{self.paciente.nombre},{self.paciente.apellido}({self.fecha})'



class HistorialMedico(models.Model):
  observaciones = models.TextField()
  paciente = models.ForeignKey(Paciente,on_delete=models.CASCADE)
  fecha = models.DateTimeField(auto_now_add=True)
  def __str__(self):
    return f'{self.paciente.apellido}-{self.paciente.nombre}Observaciones:{self.fecha}'





#Modelos relacionados con ventas
DISTANCIA = [
  ('Lejos', 'Lejos'),
  ('Cerca', 'Cerca'),
]
LADO = [
  ('Izquierda', 'Izquierda'),
  ('Derecha', 'Derecha'),
]
class Lente(models.Model):
  nombre = models.CharField(max_length=40)
  imagen = models.ImageField(null=True)
  armazon = models.BooleanField()
  distancia = models.CharField(max_length=30,choices=DISTANCIA,default='Cerca')
  lado = models.CharField(max_length=20,choices=LADO,null=True,blank=True)
  precio = models.FloatField(null=True)
  def __str__(self):
    return self.nombre



class Producto(models.Model):
  nombre = models.CharField(max_length=40)
  imagen = models.ImageField(null=True)
  precio = models.FloatField()
 
  def __str__(self):
    return self.nombre



METODOS = [
  ('Tarjeta de crédito','Tarjeta de crédito'),
  ('Tarjeta de débito','Tarjeta de débito'),
  ('Billetera virtual','Billetera virtual'),
  ('Efectivo','Efectivo'),
]
ESTADOS = [
  ('Pendiente','Pendiente'),
  ('Pedido','Pedido'),
  ('Taller','Taller'),
  ('Finalizado','Finalizado'),
]
class Pedido(models.Model):
  vendedor = models.ForeignKey(Usuario,on_delete=models.CASCADE,null=True,blank=True)
  paciente = models.ForeignKey(Paciente,on_delete=models.CASCADE)
  productos = models.ManyToManyField(Producto,blank=True)
  lentes = models.ManyToManyField(Lente,blank=True)
  metodo_pago = models.CharField(max_length=30,choices=METODOS,default='Efectivo')
  estado = models.CharField(max_length=30,choices=ESTADOS,default='Pendiente')
  fecha = models.DateTimeField(auto_now_add=True)
  @property
  def sub_total(self):
    total = 0.0
    products = self.productos.all()
    for x in products:
      total = total + x.precio
    lents = self.lentes.all()
    for x in lents:
      total = total + x.precio
    return total
  def __str__(self):
    return f'Pedido de: {self.paciente.nombre}'
