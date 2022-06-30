from django.db import models


class Tramites(models.Model):
    nombre_tramites = models.CharField(max_length=100)
    pais = models.CharField(max_length=20)
    fecha = models.DateTimeField(null=True)
    descripcion = models.TextField(max_length=5000)
    image = models.ImageField(upload_to = 'imagenes_tramites/', blank=True, null=True)
    is_active = models.BooleanField(default=True)
    class Meta:
        verbose_name = 'Tramites'
        verbose_name_plural = 'Tramites'

    def _str_(self):
        return str(self.nombre_tramites)

