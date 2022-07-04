from django.db import models


class Tramites(models.Model):
    nombre_tramites = models.CharField(max_length=100)
    pais = models.CharField(max_length=20)
    fecha = models.DateTimeField(null=True)
    descripcion = models.TextField(max_length=20000)
    image = models.ImageField(upload_to = 'imagenes_tramites/', blank=True, null=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'Tramite'
        verbose_name_plural = 'Tramites'

    def __str__(self):
        return self.nombre_tramites

