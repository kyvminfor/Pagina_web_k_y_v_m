from django import forms
from .models import Formulario

class FormularioForm(forms.ModelForm):
    class Meta:
        model = Formulario
        fields = [
            'nombre',
            'empresa',
            'telefono',
            'email',
            'motivo_contacto',
            'forma_contacto' 
        ]
        labels = {
            'nombre': 'Nombre completo',
            'empresa': 'Nombre empresa',
            'telefono': 'Telefono',
            'email': 'Correo electronico',
            'motivo_contacto': 'Motivo de contacto',
            'forma_contacto': 'Forma de contacto',
        }
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'empresa': forms.TextInput(attrs={'class': 'form-control'}),
            'telefono': forms.NumberInput(attrs={'class': 'form-control'}),
            'email': forms.TextInput(attrs={'class': 'form-control'}),
            'motivo_contacto': forms.TextInput(attrs={'class': 'form-control'}),
            'forma_contacto': forms.Select(attrs={'class': 'form-control'}),
        }
             
