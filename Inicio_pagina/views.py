from django.shortcuts import render, redirect
from .models import Formulario
from .forms import FormularioForm  # Asumiendo que tienes un formulario asociado al modelo
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
            nombre_empresa = formulario['empresa'].value()
            if Formulario.objects.filter(empresa=nombre_empresa).exists():
                # La empresa ya existe, imprime un mensaje para depuración
                return redirect('error')
            else:
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

def error(request):
    return render(request, 'Inicio/error.html')

