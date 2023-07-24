from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import CostoProyectos

def home(request):
    # Check to see if logging in
    if request.method == 'POST':
        
        username = request.POST['username']
        password = request.POST['password']
        # Aunthenticate
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "Ha iniciado sesión correctamente")
            return redirect('home')
        else:
            messages.success(request, "Hubo un error al iniciar sesión, por favor intente de nuevo...")
            return redirect('home')
    else:
        return render(request, 'core/home.html', {})


def logout_user(request):
    logout(request)
    #messages.success(request, "Ha cerrado sesión.")
    return redirect('home')

def ver_datos(request):
    if request.user.is_authenticated:
        costoProyectos = CostoProyectos.objects.all
        return render(request, 'core/ver-datos.html', {'costoProyectos':costoProyectos})
    else:
        return redirect('home')
    
def detalle_datos(request, pk):
    if request.user.is_authenticated:
        # Look Up Records
        proyecto_filtrado = CostoProyectos.objects.get(id=pk)
        return render(request, 'core/detalle-datos.html', {'proyecto_filtrado':proyecto_filtrado})
    else:
        messages.success(request, "Debe iniciar sesión para visualizar un registro.")
        return redirect('home')
    
def borrar_datos(request, pk):
    if request.user.is_authenticated:
        # Look Up Records
        proyecto_borrar = CostoProyectos.objects.get(id=pk)
        proyecto_borrar.delete()
        messages.success(request, "El registro ha sido borrado.")
        return redirect('ver-datos')
    else:
        messages.success(request, "Debe iniciar sesión para borrar un registro.")
        return redirect('home')
    
def insertar_datos(request):
    return render(request, 'core/insertar-datos.html', {})




