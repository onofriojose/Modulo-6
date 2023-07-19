from django.db import models

# Create your models here.
# Creando la clase vehiculo
class Vehiculo(models.Model):
    # lista para limitar las marcas a 4 
    marcaOpciones = [
        ('Fiat', 'Fiat'),
        ('Chevrolet', 'Chevrolet'),
        ('Ford', 'Ford'),
        ('Toyota', 'Toyota'),
    ]
    # lista para limitar las opciones a 4 
    categoriaOpciones = [
        ('Particular', 'Particular'),
        ('Transporte', 'Transporte'),
        ('Carga', 'Carga'),
    ]

    marca = models.CharField(max_length=20, default='Ford', choices=marcaOpciones) #el valor asignado a choices debe ser una lista o tupla que contenga las opciones disponibles para el campo, en este caso marcaOpciones
    modelo = models.CharField(max_length=100)
    serial_carroceria = models.CharField(max_length=50)
    serial_motor = models.CharField(max_length=50)
    categoria = models.CharField(max_length=20, default='Particular', choices=categoriaOpciones)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_modificacion = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = 'Vehiculo'
        verbose_name_plural = 'Vehiculos'
        #creando el permiso visualizar_catalogo -> se agrega despues en la funcion de registro de views (Ahora pertenece al grupo de New_Users y se le asigna a todos los usuarios que se registren)
        permissions = [
            ('visualizar_catalogo', 'puede visualizar Catálogo de Vehículos'),
        ]

    def __str__(self):
        return f"{self.marca} - {self.modelo}"
