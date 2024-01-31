# Generated by Django 4.2.1 on 2024-01-31 17:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Inicio_pagina', '0002_alter_formulario_empresa'),
    ]

    operations = [
        migrations.CreateModel(
            name='FormularioPersonas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=150)),
                ('profesion', models.CharField(max_length=80)),
                ('cv', models.FileField(upload_to='cv/')),
                ('linkedin_url', models.URLField()),
            ],
        ),
    ]
