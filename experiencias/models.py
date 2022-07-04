from tkinter import Widget
from django.db import models
from cuenta.models import User

class Experiencias (models.Model):
    titulo = models.CharField(max_length=100)
    pais = models.CharField(max_length=50)
    fecha = models.DateTimeField(null=True)
    autor = models.CharField(max_length=50)
    cuerpo = models.TextField(max_length=20000)
    image = models.ImageField(upload_to = 'imagenes_experiencias/', blank=True, null=True)
    is_active = models.BooleanField(default=True)
    class Meta:
        verbose_name = 'Experiencia'
        verbose_name_plural = 'Experiencias'

    def __str__(self):
        return str(self.titulo)

