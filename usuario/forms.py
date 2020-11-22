from django.contrib.auth.forms import AuthenticationForm
from django import forms
from .models import Usuario


class FormularioLogin(AuthenticationForm):
  def __init__(self, *args, **kwargs):
    super(FormularioLogin, self).__init__(*args, **kwargs)
    self.fields['username'].widget.attrs['class'] = 'form-control'
    self.fields['username'].widget.attrs['placeholder'] = 'Introduzca usuario'
    self.fields['password'].widget.attrs['class'] = 'form-control'
    self.fields['password'].widget.attrs['placeholder'] = 'Introduzca Contraseña'






class FormularioUsuario(forms.ModelForm):
  password1 = forms.CharField(label="contraseña", widget=forms.PasswordInput(
    attrs={
      'class': 'form-control',
      'id': 'password1',
      'placeholder': 'Contraseña',
      'required': 'required'
    }
  ))
  password2 = forms.CharField(label="contraseña confirmacion", widget=forms.PasswordInput(
    attrs={
      'class': 'form-control',
      'id': 'password2',
      'placeholder': 'Confirmar contraseña',
      'required': 'required'
    }
  ))
  class Meta:
    model = Usuario
    fields = ('email','username','nombres','apellidos','rol')
    widgets = {
      'email': forms.EmailInput(
        attrs={
          'class': 'form-control',
          'placeholder': 'Email',
        }
      ),
      'nombres': forms.TextInput(
        attrs={
          'class': 'form-control',
          'placeholder': 'Nombres',
        }
      ),
      'apellidos': forms.TextInput(
        attrs={
          'class': 'form-control',
          'placeholder': 'Apellidos',
        }
      ),
      'username': forms.TextInput(
        attrs={
          'class': 'form-control',
          'placeholder': 'Username',
        }
      ),
      'rol': forms.Select(
        attrs={'class':'form-control'}
      )
    }

  def clean_password2(self):
    #validacion para la contraseña(que ambas contraseñas sean iguales)
    password2 = self.cleaned_data['password2']
    password1 = self.cleaned_data['password1']
    if password1 != password2:
      raise forms.ValidationError("Las contraseñas no coinciden")
    return password2

  def save(self, commit=True):
    user = super().save(commit=False)
    user.set_password(self.cleaned_data['password1'])
    if commit:
      user.save()
    return user