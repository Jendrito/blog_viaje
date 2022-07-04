from django.db import models

class Contacto(models.Model):
    nombre_contacto = models.CharField(max_length=30)
    pais_contacto = models.CharField(max_length=20)
    correo_contacto = models.CharField(max_length=50)
    consulta = models.CharField(max_length=500)

    class Meta:
        verbose_name = 'Contacto'
        verbose_name_plural = 'Contactos'

    def __str__(self):
        return str(self.nombre_contacto)