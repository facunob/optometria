from django.shortcuts import render
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.decorators.cache import never_cache
from django.views.decorators.csrf import csrf_protect
from django.views.generic.edit import FormView
from django.contrib.auth import login, logout
from django.http import HttpResponseRedirect
from django.views.generic import CreateView
from .forms import FormularioLogin, FormularioUsuario
from .models import Usuario

class Login(FormView):
  template_name = 'usuarios/login.html'
  form_class = FormularioLogin
  success_url = reverse_lazy('home')

  @method_decorator(never_cache)
  @method_decorator(csrf_protect)
  def dispatch(self, request, *args, **kwargs):
    if request.user.is_authenticated:
      return HttpResponseRedirect(self.get_success_url())
    else:
      return super(Login, self).dispatch(request, *args, **kwargs)

  def form_valid(self, form):
    login(self.request, form.get_user())
    return super(Login, self).form_valid(form)


def logoutUser(request):
  logout(request)
  return HttpResponseRedirect('/')




class RegistrarUsuario(CreateView):
  model = Usuario
  form_class = FormularioUsuario
  template_name = 'usuarios/registrar_usuario.html'
  success_url = reverse_lazy('login')