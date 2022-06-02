from django.urls import path

from experiencias.views import ver_experiencias

urlpatterns =[
    path('ver-experiencias/', ver_experiencias, name = 'ver-experiencias'),
]