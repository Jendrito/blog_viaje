from email.policy import default
from multiprocessing.sharedctypes import Value
from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    telefono = models.CharField(max_length=20)
    imagen = models.ImageField(upload_to='profile_image', blank = True)
    redes_sociales = models.CharField(max_length=100)
    
    class Meta:
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'
    
    def str(self):
        return str(self.username)
 
