from django.db import models

class Formulario(models.Model):
    OPCIONES_CONTACTO = [
        ('telefono', 'Comunicarse por teléfono'),
        ('email', 'Comunicarse por email'),
    ]

    nombre = models.CharField(max_length=50)
    empresa = models.CharField(max_length=100, blank=True, null=True, default=None)  # Cambios aquí
    telefono = models.IntegerField()
    email = models.CharField(max_length=150)
    motivo_contacto = models.CharField(max_length=400)
    forma_contacto = models.CharField(max_length=20, choices=OPCIONES_CONTACTO)

    def __str__(self):
        return self.empresa
