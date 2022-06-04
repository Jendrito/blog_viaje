from django.urls import path

from tramites.views import ver_tramites, crear_tramites
urlpatterns =[
    path('ver-tramites/', ver_tramites, name = 'ver-tramites'),
    path('crear-tramites/', crear_tramites, name = 'crear-tramites'),
]