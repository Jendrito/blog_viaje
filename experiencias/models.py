from django.db import models

class Experiencias (models.Model):
    titulo = models.CharField(max_length=100)
    pais = models.CharField(max_length=50)
    fecha = models.DateTimeField()
    autor = models.CharField(max_length=50)
    cuerpo = models.CharField(max_length=10000)

