from django import forms
from .models import Vehiculo
from django.core.validators import MaxValueValidator, MinValueValidator

class VehiculoForm(forms.ModelForm):
    precio = forms.DecimalField(
        label='Precio',
        help_text='Precio minimo 0',
        validators=[MaxValueValidator(99999999), MinValueValidator(0)]
    )
        
    class Meta:
        model = Vehiculo
        fields = ['marca', 'modelo', 'serial_carroceria', 'serial_motor', 'categoria', 'precio']
        widgets = {
            'modelo': forms.TextInput(attrs={'class': 'form-control', 'style': 'width: 300px'}),
            'serial_carroceria': forms.TextInput(attrs={'class': 'form-control', 'style': 'width: 300px'}),
            'serial_motor': forms.TextInput(attrs={'class': 'form-control', 'style': 'width: 300px'}),
            'precio': forms.NumberInput(attrs={'class': 'form-control', 'style': 'width: 300px'})
        }