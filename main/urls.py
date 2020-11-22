from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required

urlpatterns = [
    #Página de inicio
    path('', views.Home.as_view(), name='home'),
    #Urls relacionadas con pacientes
    path('listado_pacientes/', views.ListadoPacientes.as_view(),name='listado_pacientes'),
    path('agregar_paciente/', views.agregarPaciente,name='agregar_paciente'),
    #Urls relacionadas con turnos(necesarias para el rol: Secretaría)
    path('crear_turno/',views.crearTurno,name='crear_turno'),
    path('listado_turnos/', views.ListadoTurnos.as_view(),name='listado_turnos'),
    path('eliminar_turno/<pk>/', views.EliminarTurno.as_view(),name='eliminar_turno'),
    path('modificar_turno/<int:pk>/', views.modificarTurno,name='modificar_turno'),
    path('marcar_asistencia/<int:pk>/',views.marcarAsistencia,name='marcar_asistencia'),
    #Urls relacionadas con personal medico:
    path('listado_turnos_asignados/', views.listadoTurnosAsignados,name='listado_turnos_asignados'),
    path('listado_historial_medico/<int:pk>/', views.listadoHistorialMedico,name='listado_historial_medico'),
    #Urls relacionadas con ventas
    path('listado_productos/', views.listadoProductos,name='listado_productos'),
    path('crear_pedido/',views.crearPedido,name='crear_pedido'),
    path('listado_pedidos/', views.ListadoPedidos.as_view(),name='listado_pedidos'),
    path('detalle_pedido/<int:pk>/',views.detallePedido,name='detalle_pedido'),
    #Urls relacionadas con el rol de taller
    path('pedidos_taller/',views.pedidosTaller,name='pedidos_taller'),
    path('detalle_pedido_taller/<int:pk>/',views.detallePedidoTaller,name='detalle_pedido_taller'),
    #Urls relacionadas con Gerencia
    path('turnos_no_asistidos/', views.turnosNoAsistidos,name='turnos_no_asistidos'),
    path('turnos_asistidos/', views.turnosAsistidos,name='turnos_asistidos'),
    path('pacientes_compra/',views.pacientesCompra,name='pacientes_compra'),
    path('ventas/',views.ventas,name='ventas'),
    path('productos/',views.productos,name='productos'),
]