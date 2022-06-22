from distutils.command.upload import upload
from email.policy import default
from multiprocessing.sharedctypes import Value
from xml.etree.ElementInclude import default_loader
from django.db import models
from django.contrib.auth.models import User

class User_profile(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE, related_name='user_profile')
    telefono = models.CharField(max_length=20)
    imagen = models.ImageField(upload_to='profile_image' )

    class Meta:
        verbose_name = 'perfil de usuario'
        verbose_name_plural = 'perfiles de usuario'

    def __str__(self):
        return str(self.usuario)