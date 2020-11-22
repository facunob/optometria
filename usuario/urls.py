from django.urls import path
from django.contrib.auth.decorators import login_required
from .views import RegistrarUsuario, Login, logoutUser

urlpatterns = [
  path('registrar_usuario', RegistrarUsuario.as_view(), name='registrar_usuario' ),
  path('accounts/login/', Login.as_view() , name = 'login'),
  path('logout/', login_required(logoutUser) , name = 'logout'),
]