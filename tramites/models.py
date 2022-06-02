from django.db import models

class Tramites(models.Model):
    nombre_tramites = models.CharField(max_length=100)
    pais = models.CharField(max_length=20)
    descripcion = models.CharField(max_length=5000)
