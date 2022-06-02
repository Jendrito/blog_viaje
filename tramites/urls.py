from django.urls import path

from tramites.views import ver_tramites
urlpatterns =[
    path('ver-tramites/', ver_tramites, name = 'ver-tramites'),
]