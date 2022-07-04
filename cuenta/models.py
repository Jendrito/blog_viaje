from email.policy import default
from multiprocessing.sharedctypes import Value
from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    descripcion = models.CharField(max_length=100, blank=True, null=True)
    telefono = models.IntegerField(null=True, blank=True)
    redes_sociales = models.URLField(max_length=100, null=True, blank=True)
    image = models.ImageField(upload_to = 'imagenes_User/', blank=True, null=True )

    class Meta:
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'

    def __str__(self):
        return str(self.username)
    

