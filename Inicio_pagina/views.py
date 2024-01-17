from django.shortcuts import render, redirect
from .models import Formulario
from .forms import FormularioForm  # Asumiendo que tienes un formulario asociado al modelo

def inicio(request):
    return render(request, 'home.html')

def productos(request):
    return render(request, 'Inicio/productos.html')

def soluciones(request):
    return render(request, 'Inicio/soluciones.html')

def precios(request):
    return render(request, 'Inicio/precios.html')

def contacto(request):
    if request.method == 'POST':
        formulario = FormularioForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect('inicio')  # Puedes redirigir a donde desees después de guardar
    else:
        formulario = FormularioForm()

    return render(request, 'Inicio/contacto.html', {'formulario': formulario})
