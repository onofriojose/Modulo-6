from django.conf import settings
from django.urls import path
from .views import IndexPageView, vehiculo_add, lista_vehiculos, registro, ingreso, editar_vehiculo, eliminar_vehiculo, salir

urlpatterns = [
    path('', IndexPageView.as_view(), name='index'),
    path('vehiculo/add/', vehiculo_add, name='vehiculoAdd'),
    path('lista_vehiculos/', lista_vehiculos, name='lista_vehiculos'),
    path('registro/', registro, name='registro'),
    path('login/', ingreso, name='login'),
    path('logout/', salir, name='logout'),
    path('editar_vehiculo/<int:vehiculo_id>', editar_vehiculo, name='editar_vehiculo'),
    path('eliminar_vehiculo/<int:vehiculo_id>', eliminar_vehiculo, name='eliminar_vehiculo'),
]