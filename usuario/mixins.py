from django.shortcuts import redirect
from django.contrib import messages

class SecretariaMixin(object):
  def dispatch(self,request,*args,**kwargs):
    if request.user.is_authenticated:
      if (request.user.rol == 'Secretaría'):
        return super().dispatch(request,*args,**kwargs)
    messages.error(request, 'Para realizar esta acción debes ser un secretario.')
    return redirect('home')

class LoginUserMixin(object):
  def dispatch(self,request,*args,**kwargs):
    if request.user.is_authenticated:
        return super().dispatch(request,*args,**kwargs)
    messages.error(request, 'Para realizar esta acción debes estar logeado.')
    return redirect('login')
