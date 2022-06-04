from django.urls import path

from experiencias.views import ver_experiencias, crear_experiencias

urlpatterns =[
    path('ver-experiencias/', ver_experiencias, name = 'ver-experiencias'),
    path('crear-experiencias/', crear_experiencias, name = 'crear-experiencias')
]