import email
from multiprocessing import managers
from multiprocessing.sharedctypes import Value
from django.db import models
from django.contrib.auth.models import User

class PerfilUsuario(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE, related_name='usuario')
    telefono = models.CharField(max_length=20)
    imagen = models.ImageField(upload_to='blog_viaje', default='usuario.jpg')
    redes_sociales = models.CharField(max_length=100)
 

    def _str_(self):
        return str(self.usuario)

    class Meta:
        verbose_name = 'PerfilUsuario'
        verbose_name_plural = 'PerfilUsuarios'