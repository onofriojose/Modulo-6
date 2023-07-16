from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType
from django.db.models import Q
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.views.generic import TemplateView
from .forms import VehiculoForm
from .models import Vehiculo
import datetime
from django.contrib.auth.models import Group #para crear usuarios nuevos y asignarle el grupo New_User que cree en el sitio administrativo con los permisos pra interactuar con la tabla Vehiculo y visualizar catalogo
# Create your views here.
class IndexPageView(TemplateView):
    template_name = 'index.html'


@login_required
def vehiculo_add(request):
    if request.method == 'POST':
        form = VehiculoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Vehiculo creado exitosamente')
            return redirect('lista_vehiculos')
        else:
            messages.error(request, 'Modificar datos de ingreso')  # crear mensaje de error
            return HttpResponseRedirect(reverse('vehiculoAdd'))
    else:
        form = VehiculoForm()
    return render(request, 'vehiculoAdd.html', {'form': form})

@login_required
def lista_vehiculos(request):
    vehiculos = Vehiculo.objects.all()
    for vehiculo in vehiculos:
        vehiculo.rango_precio = rango_precio(vehiculo)
    return render(request, 'lista_vehiculos.html', {'vehiculos': vehiculos})

def rango_precio(obj):
    if obj.precio < 10000:
        return 'Bajo'
    elif 10000 <= obj.precio < 30000:
        return 'Medio'
    else:
        return 'Alto'


from django.contrib.auth.models import Group

def registro(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()  #guardar el usuario registrado
            group = Group.objects.get(name='New_Users')  #aqui se obtiene el grupo New_Users que cree en el sitio administrativo
            user.groups.add(group)  #agregar al usuario al grupo New_Users
            
            '''paso a comentar estas lineas porque ahora el grupo de New_Users se encarga de asignarle este mismo permiso a todos los usuarios nuevos
            #asignar el permiso "visualizar_catalogo" al usuario
            content_type = ContentType.objects.get_for_model(Vehiculo)
            permission = Permission.objects.get(
                codename='visualizar_catalogo', content_type=content_type
            )
            user.user_permissions.add(permission) #con user_permissions.add se agrega el permiso visualizar_catalogo a los usuarios que se registren
            '''
            messages.success(request, 'Registrado exitosamente')
            return redirect('login')
        else:
            messages.error(request, 'No se ha registrado el usuario')
            return HttpResponseRedirect(reverse('registro'))
    else:
        form = UserCreationForm()
        return render(request, 'registro.html', {'form': form})


def ingreso(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('lista_vehiculos')
        else:
            messages.error(request, 'Credenciales inválidas')
            return render(request, 'login.html')
    return render(request, 'login.html')

@login_required
def editar_vehiculo(request, vehiculo_id):
    vehiculo = get_object_or_404(Vehiculo, id=vehiculo_id)
    if request.method == 'POST':
        form = VehiculoForm(request.POST, instance=vehiculo)
        if form.is_valid():
            vehiculo = form.save(commit=False) 
            vehiculo.fecha_modificacion = datetime.datetime.now()
            vehiculo.save()
            messages.success(request, 'Vehiculo editado exitosamente')
            return redirect('lista_vehiculos')
        else:
            messages.error(request, 'Error editando vehiculo')
            return HttpResponseRedirect(reverse('editar_vehiculo', args=[vehiculo_id]))
    else:
        form = VehiculoForm(instance=vehiculo)
        return render(request, 'editar_vehiculo.html', {'form': form, 'vehiculo_id': vehiculo_id})

@login_required    
def eliminar_vehiculo(request, vehiculo_id):
    vehiculo = get_object_or_404(Vehiculo, id=vehiculo_id)  # obterner vehiculo eb la db mediante id
    vehiculo.delete()
    messages.info(request, 'Vehiculo eliminado exitosamente')
    return redirect('lista_vehiculos')

def salir(request):
    logout(request)
    return render(request, 'login.html')