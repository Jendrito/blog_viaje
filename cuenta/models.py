import email
from multiprocessing import managers
from multiprocessing.sharedctypes import Value
from django.db import models
from django.contrib.auth.models import User

class PerfilUsuario(models.Model):
    username = models.OneToOneField(User, on_delete=models.CASCADE, related_name='username')
    telefono = models.CharField(max_length=20)
    imagen = models.ImageField(null = Value)
    email = models.OneToOneField(User, on_delete=models.CASCADE, related_name='email')
    redes_sociales = models.CharField(max_length=100)
    password = models.OneToOneField(User, on_delete=models.CASCADE, related_name='password')
    