import datetime
from django.contrib.auth.forms import AuthenticationForm
from django import forms
from .models import Paciente,Turno,HistorialMedico,Pedido,Lente,Producto
from usuario.models import Usuario



#Formulario para crear un nuevo paciente
class PacienteForm(forms.ModelForm):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)   

    class Meta:
        model = Paciente
        fields = ['nombre','apellido','dni','obra_social']
        widgets = {
            'nombre': forms.TextInput(
                attrs={
                    'class':'form-control'
                }
            ),
            'apellido': forms.TextInput(
                attrs={
                    'class':'form-control'
                }
            ),
            'dni': forms.TextInput(
                attrs={
                    'class':'form-control'
                }
            ),
            'obra_social': forms.TextInput(
                attrs={
                    'class':'form-control'
                }
            ),
           
        }







class ObservacionesForm(forms.ModelForm):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs) 
        self.fields['paciente'].queryset = Paciente.objects.all()

    class Meta:
        model = HistorialMedico
        fields = ['observaciones','paciente']
        widgets = {
            'observaciones': forms.Textarea(
                attrs={
                    'class':'form-control'
                }
            ),
            'paciente': forms.Select(
                attrs={
                    'class':'form-control'
                }
            ),   
        }


class PedidoForm(forms.ModelForm):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs) 
        self.fields['paciente'].queryset = Paciente.objects.all()
        self.fields['lentes'].queryset = Lente.objects.all()
        self.fields['productos'].queryset = Producto.objects.all()

    class Meta:
        model = Pedido
        fields = ['paciente','productos','lentes','metodo_pago']
        widgets = {
            'productos': forms.SelectMultiple(
                attrs={
                    'class':'form-control'
                }
            ),
            'lentes': forms.SelectMultiple(
                attrs={
                    'class':'form-control'
                }
            ),
            'paciente': forms.Select(
                attrs={
                    'class':'form-control'
                }
            ),
            'metodo_pago': forms.Select(
                attrs={
                    'class':'form-control'
                }
            ),    
        }




