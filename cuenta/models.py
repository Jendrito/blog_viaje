from multiprocessing.sharedctypes import Value
from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    descripcion = models.CharField(max_length=100)
    telefono = models.IntegerField(null = Value)
    redes_sociales = models.CharField(max_length=100, null = Value)
    


