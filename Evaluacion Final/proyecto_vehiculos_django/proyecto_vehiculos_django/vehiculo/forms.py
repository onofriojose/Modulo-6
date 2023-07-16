from django import forms
from .models import Vehiculo

class VehiculoForm(forms.ModelForm):
    class Meta:
        model = Vehiculo
        fields = ['marca', 'modelo', 'serial_carroceria', 'serial_motor', 'categoria', 'precio']
        widgets = {
            'modelo': forms.TextInput(attrs={'class': 'form-control', 'style': 'width: 300px'}),
            'serial_carroceria': forms.TextInput(attrs={'class': 'form-control', 'style': 'width: 300px'}),
            'serial_motor': forms.TextInput(attrs={'class': 'form-control', 'style': 'width: 300px'}),
            'precio': forms.NumberInput(attrs={'class': 'form-control', 'style': 'width: 300px'})
        }