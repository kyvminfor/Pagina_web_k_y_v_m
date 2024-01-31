from django.shortcuts import render, redirect
from .models import Formulario
from .models import FormularioPersonas  # Importa el modelo
from .forms import FormularioForm  # Asumiendo que tienes un formulario asociado al modelo
from .forms import FormularioPersonasForm
from django.core.mail import send_mail
from django.conf import settings


def inicio(request):
    return render(request, 'home.html')

def productos(request):
    return render(request, 'Inicio/productos.html')

def soluciones(request):
    return render(request, 'Inicio/soluciones.html')


def contacto(request):
    if request.method == 'POST':
        formulario = FormularioForm(request.POST)
        if formulario.is_valid():
            formulario.save()

            # Envía el correo electrónico
            enviar_correo(formulario.cleaned_data)

            return redirect('confirmacion')
    else:
        formulario = FormularioForm()

    return render(request, 'Inicio/contacto.html', {'formulario': formulario})


def enviar_correo(datos_formulario):
    asunto = 'Nueva solicitud de contacto'
    mensaje = f'Nombre: {datos_formulario["nombre"]}\n' \
              f'Empresa: {datos_formulario["empresa"]}\n' \
              f'Teléfono: {datos_formulario["telefono"]}\n' \
              f'Email: {datos_formulario["email"]}\n' \
              f'Motivo de contacto: {datos_formulario["motivo_contacto"]}\n' \
              f'Forma de contacto preferida: {datos_formulario["forma_contacto"]}'

    send_mail(
        asunto,
        mensaje,
        settings.EMAIL_HOST_USER,  # Remitente
        ['kkvm992@gmail.com'],  # Destinatario(s)
        fail_silently=False,
    )
def confirmacion(request):
    return render(request, 'Inicio/confirmacion_formulario.html')


def form_personas(request):
    if request.method == 'POST':
        formulario = FormularioPersonasForm(request.POST, request.FILES)  # Asegúrate de manejar archivos adjuntos
        if formulario.is_valid():
            formulario.save()
            # No olvides realizar las acciones adicionales que necesites aquí, como enviar correos electrónicos, etc.
            return redirect('confirmacion_2')
    else:
        formulario = FormularioPersonasForm()

    return render(request, 'Inicio/form_personas.html', {'formulario': formulario})

def confirmacion_2(request):
    return render(request, 'Inicio/confirmacion_formulario_2.html')