from tkinter import Widget
from django.db import models
from cuenta.models import User

class Experiencias (models.Model):
    titulo = models.CharField(max_length=100)
    pais = models.CharField(max_length=50)
    fecha = models.DateTimeField(null=True)
    autor = models.CharField(max_length=50)
    cuerpo = models.TextField(max_length=10000)
    image = models.ImageField(upload_to = 'imagenes_experiencias/', blank=True, null=True)
    is_active = models.BooleanField(default=True)
    class Meta:
        verbose_name = 'Experiencias'
        verbose_name_plural = 'Experiencias'

    def _str_(self):
        return self.titulo

