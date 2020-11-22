import json
import datetime
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, CreateView, DeleteView, UpdateView, DetailView
from .models import Paciente, Turno, HistorialMedico, Lente, Producto, Pedido
from .forms import PacienteForm, ObservacionesForm, PedidoForm
from usuario.mixins import LoginUserMixin, SecretariaMixin
from usuario.models import Usuario


#Vista de inicio
class Home(LoginUserMixin, TemplateView):
  template_name = 'home.html'



#Vistas para ver y crear pacientes(Secretaría)
class ListadoPacientes(ListView):
  model = Paciente
  template_name = 'listado_pacientes.html'

class AgregarPaciente(CreateView):
  model = Paciente
  template_name = 'agregar_paciente.html'
  form_class = PacienteForm
  success_url = reverse_lazy('listado_pacientes')

def agregarPaciente(request):
  form = PacienteForm()
  if (request.method == 'POST'):
    formulario = PacienteForm(request.POST)
    if formulario.is_valid():
      nombre = formulario.cleaned_data['nombre']
      apellido = formulario.cleaned_data['apellido']
      dni = formulario.cleaned_data['dni']
      obra_social = formulario.cleaned_data['obra_social']
      paciente = Paciente.objects.create(nombre=nombre,apellido=apellido,dni=dni,obra_social=obra_social)
      historialMedico = HistorialMedico.objects.create(paciente=paciente,observaciones='Paciente recién ingreado')
      historialMedico.save()
      return redirect('listado_pacientes')
  return render(request,'agregar_paciente.html',{'form':form})





#Vistas para ver, crear, editar y eliminar turnos(Secretaría)
def crearTurno(request):
  pacientes = Paciente.objects.all()
  medicos = Usuario.objects.filter(rol='Profesional médico')
  if (request.method == 'POST'):
    pacienteid = request.POST['paciente']
    paciente = Paciente.objects.get(id=pacienteid)
    medicoid = request.POST['medico']
    medico = Usuario.objects.get(id=medicoid)
    fecha = request.POST['fecha']
    turno = Turno.objects.create(medico=medico,paciente=paciente,fecha=fecha)
    turno.save()
    return redirect('listado_turnos')
  return render(request,'crear_turno.html',{'pacientes':pacientes,'medicos':medicos})


class ListadoTurnos(ListView):
  model = Turno 
  template_name = 'listado_turnos.html'
  def get_queryset(self):
    return self.model.objects.filter(asistencia=False).order_by('fecha')
  


class EliminarTurno(DeleteView):
  model = Turno
  success_url = reverse_lazy('listado_turnos')

def modificarTurno(request,pk):
  pacientes = Paciente.objects.all()
  medicos = Usuario.objects.filter(rol='Profesional médico')
  if (request.method == 'POST'):
    pacienteid = request.POST['paciente']
    paciente = Paciente.objects.get(id=pacienteid)
    medicoid = request.POST['medico']
    medico = Usuario.objects.get(id=medicoid)
    fecha = request.POST['fecha']
    turno = Turno.objects.get(id=pk)
    turno.fecha = fecha
    turno.paciente = paciente
    turno.medico = medico
    turno.save()
    return redirect('listado_turnos')
  return render(request,'modificar_turno.html',{'pacientes':pacientes,'medicos':medicos,'id':pk})

def marcarAsistencia(request,pk):
  turno = Turno.objects.get(id=pk)
  turno.asistencia = True
  turno.save()
  return redirect('listado_turnos')





#Vistas para el profesional médico:
def listadoTurnosAsignados(request):
  fecha_actual = datetime.datetime.now()
  turnos = Turno.objects.filter(medico=request.user,fecha__gte=fecha_actual)
  contexto = {'turnos':turnos}
  if (request.method == 'POST'):
    if (request.POST['anio']):
      if(request.POST['mes']):
        anio = request.POST['anio']
        mes = request.POST['mes']
        turnos = Turno.objects.filter(medico=request.user,fecha__gte=fecha_actual,fecha__month=mes,fecha__year=anio)
        contexto = {'turnos':turnos}
        return render(request,'listado_turnos_asignados.html',contexto)
    if (request.POST['anio']):
      anio = request.POST['anio']
      turnos = Turno.objects.filter(medico=request.user,fecha__gte=fecha_actual,fecha__year=anio)
      contexto = {'turnos':turnos}
      return render(request,'listado_turnos_asignados.html',contexto)
    if (request.POST['mes']):
      mes = request.POST['mes']
      turnos = Turno.objects.filter(medico=request.user,fecha__gte=fecha_actual,fecha__month=mes,fecha__year=fecha_actual.year)
      contexto = {'turnos':turnos}
      return render(request,'listado_turnos_asignados.html',contexto)
  return render(request,'listado_turnos_asignados.html',contexto)



def listadoHistorialMedico(request,pk):
  paciente = Paciente.objects.get(id=pk)
  if (HistorialMedico.objects.filter(paciente=paciente)):
    historialMedico = HistorialMedico.objects.filter(paciente=paciente)
    contexto = {'historialMedico':historialMedico}
  else:
    historialMedico = HistorialMedico.objects.create(paciente=paciente)
    historialMedico.save()
    contexto = {'historialMedico':historialMedico}
  if (request.method == 'POST'):
    obs = request.POST['obs']
    historial = HistorialMedico.objects.create(paciente=paciente,observaciones=obs)
    historial.save()
  return render(request,'listado_historial_medico.html',contexto)



#Vista de ventas
def listadoProductos(request):
  lentes = Lente.objects.all()
  productos = Producto.objects.all()
  contexto={'lentes':lentes,'productos':productos}
  return render(request,'listado_productos.html',contexto)


def crearPedido(request):
  pacientes = Paciente.objects.all()
  lentes = Lente.objects.all()
  productos = Producto.objects.all()
  contexto = {'pacientes':pacientes,'productos':productos,'lentes':lentes}
  if (request.method == 'POST'):
    pacientex = request.POST['paciente']
    paciente = Paciente.objects.get(nombre=pacientex)
    productos = request.POST.getlist('productos', False)
    lentes = request.POST.getlist('lentes',False)
    metodo_pago = request.POST['metodo_pago']
    pedido = Pedido.objects.create(vendedor=request.user,paciente=paciente,metodo_pago=metodo_pago)
    if (productos):
      for producto in productos:
        prod = Producto.objects.get(nombre=producto)
        pedido.productos.add(prod)
    if (lentes):
      for lente in lentes:
        lent = Lente.objects.get(nombre=lente)
        pedido.lentes.add(lent)
    pedido.save()
    return redirect('listado_pedidos')
  return render(request,'crear_pedido.html',contexto)


class ListadoPedidos(ListView):
  model = Pedido
  template_name = 'listado_pedidos.html'


def detallePedido(request,pk):
  pedido = Pedido.objects.get(id=pk)
  if (request.method == 'POST'):
    estado = request.POST['estado']
    pedido.estado = estado
    pedido.save()
    return redirect('listado_pedidos')
  return render(request,'detalle_pedido.html',{'pedido':pedido})



#Vistas para el rol de taller
def pedidosTaller(request):
  pedidos = Pedido.objects.filter(estado='Taller')
  return render(request,'pedidos_taller.html',{'pedidos':pedidos})

def detallePedidoTaller(request,pk):
  pedido = Pedido.objects.get(id=pk)
  if (request.method == 'POST'):
    #estado = request.POST['estado']
    pedido.estado = 'Finalizado'
    pedido.save()
    return redirect('pedidos_taller')
  return render(request,'detalle_pedido_taller.html',{'pedido':pedido})



#vistas para gerencia
def turnosNoAsistidos(request):
  dia = datetime.datetime.now()
  semana = dia - datetime.timedelta(days=7)
  anio = datetime.datetime.now().year
  mes = datetime.datetime.now().month 
  hoy = dia.day
  turnos_ausentes = Turno.objects.filter(asistencia=False,fecha__year=anio,fecha__month=mes,fecha__day__lte=hoy)
  turnos_ausentes_semana = Turno.objects.filter(asistencia=False,fecha__gte=semana,fecha__lte=dia)
  return render(request,'turnos_no_asistidos.html',{'turnos_mes':turnos_ausentes,'turnos_semana':turnos_ausentes_semana})

def turnosAsistidos(request):
  dia = datetime.datetime.now()
  semana = dia - datetime.timedelta(days=7)
  anio = datetime.datetime.now().year
  mes = datetime.datetime.now().month 
  hoy = dia.day
  turnos= Turno.objects.filter(asistencia=True,fecha__year=anio,fecha__month=mes,fecha__day__lte=hoy)
  turnos_semana = Turno.objects.filter(asistencia=True,fecha__gte=semana,fecha__lte=dia)
  return render(request,'turnos_asistidos.html',{'turnos_mes':turnos,'turnos_semana':turnos_semana})

def pacientesCompra(request):
  dia = datetime.datetime.now()
  semana = dia - datetime.timedelta(days=7)
  pedidos_mes = Pedido.objects.filter(fecha__year=dia.year,fecha__month=dia.month)
  pedidos_semana = Pedido.objects.filter(fecha__gte=semana,fecha__lte=dia)
  pacientes_mes = []
  for ped in pedidos_mes:
    booli = False
    for paciente in pacientes_mes:
      if (ped.paciente == paciente):
        booli = True
    if (booli == False):
      pacientes_mes.append(ped.paciente)
  pacientes_semana = []
  for ped in pedidos_semana:
    boole = False
    for paciente in pacientes_semana:
      if (ped.paciente == paciente):
        boole = True
    if (boole == False):
      pacientes_semana.append(ped.paciente)
  return render(request,'pacientes_compra.html',{'pacientes_mes':pacientes_mes,'pacientes_semana':pacientes_semana})


def ventas(request):
  dia = datetime.datetime.now()
  pedidos_mes = Pedido.objects.filter(fecha__year=dia.year,fecha__month=dia.month)
  if (request.method == 'POST'):
      mes = request.POST['mes']
      anio = request.POST['anio']
      pedidos = Pedido.objects.filter(fecha__month=mes,fecha__year=anio)
      contexto = {'pedidos':pedidos}
      return render(request,'ventas.html',contexto)
  return render(request,'ventas.html',{'pedidos':pedidos_mes})


def productos(request):
  dia = datetime.datetime.now()
  pedidos = Pedido.objects.filter(fecha__year=dia.year,fecha__month=dia.month)
  productos = {}
  for ped in pedidos:
    for x in ped.productos.all():
      booli = False
      if (productos):
        for prod in productos:
          if (x == prod):
            booli = True 
        if (booli == True):
          productos[x] += 1
          booli = False
        else:
          productos[x] = 1
      else:
          productos[x] = 1
  lentes = {}
  for ped in pedidos:
    for x in ped.lentes.all():
      boole = False
      if (lentes):
        for lent in lentes:
          if (x == lent):
            boole = True 
        if (boole == True):
          lentes[x] += 1
          boole = False
        else:
          lentes[x] = 1
      else:
          lentes[x] = 1
  return render(request,'productos.html',{'productos':productos,'lentes':lentes})
