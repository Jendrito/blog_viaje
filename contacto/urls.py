from django.urls import path

from contacto.views import contacto, exitos

urlpatterns =[
    path('contacto/', contacto, name='contacto'),
    path('exitos/', exitos, name='exitos'),
]