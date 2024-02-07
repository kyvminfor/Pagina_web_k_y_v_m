from django.shortcuts import render, redirect
from .models import Formulario
from .models import FormularioPersonas  # Importa el modelo
from .forms import FormularioForm  # Asumiendo que tienes un formulario asociado al modelo
from .forms import FormularioPersonasForm
from django.core.mail import send_mail, EmailMessage
from django.conf import settings
from django.core.mail import EmailMultiAlternatives


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
        ['informaticakyvm@gmail.com'],  # Destinatario(s)
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
            enviar_correo_trabajadores(formulario.cleaned_data)
            return redirect('confirmacion_2')
    else:
        formulario = FormularioPersonasForm()

    return render(request, 'Inicio/form_personas.html', {'formulario': formulario})

def enviar_correo_trabajadores(datos_formulario):
    asunto = 'Nueva solicitud de posible trabajador'
    mensaje_texto = f'Nombre: {datos_formulario["nombre"]}\n' \
                    f'Email: {datos_formulario["email"]}\n' \
                    f'Profesión: {datos_formulario["profesion"]}\n' \
                    f'Link de LinkedIn: {datos_formulario["linkedin_url"]}\n' \
                    f'CV Adjunto a continuación'

    # Adjuntar el archivo CV al mensaje de correo
    archivo_cv = datos_formulario["cv"]
    mensaje_html = "<p>" + mensaje_texto.replace("\n", "<br>") + "</p>"
    email = EmailMultiAlternatives(asunto, mensaje_texto, settings.EMAIL_HOST_USER, ['informaticakyvm@gmail.com'])
    email.attach_alternative(mensaje_html, "text/html")
    
    # Obtenemos el contenido del archivo adjunto
    archivo_cv_content = archivo_cv.read()
    
    # Establecemos el tipo MIME del archivo adjunto manualmente
    if archivo_cv.name.endswith('.pdf'):
        tipo_mime = 'application/pdf'
    elif archivo_cv.name.endswith(('.doc', '.docx')):
        tipo_mime = 'application/msword'
    else:
        tipo_mime = 'application/octet-stream'  # Tipo MIME genérico

    # Adjuntamos el archivo al correo con el tipo MIME adecuado
    email.attach(archivo_cv.name, archivo_cv_content, tipo_mime)
    
    # Enviar el correo
    email.send()
    
def confirmacion_2(request):
    return render(request, 'Inicio/confirmacion_formulario_2.html')