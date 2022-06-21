from django.urls import path

from experiencias.views import ver_experiencias, crear_experiencias, Delete_experiencias, Update_experiencias

urlpatterns =[
    path('ver-experiencias/', ver_experiencias, name = 'ver-experiencias'),
    path('crear-experiencias/', crear_experiencias, name = 'crear-experiencias'),
    path('borrar-experiencias/<int:pk>/', Delete_experiencias.as_view(), name = 'borrar-experiencias'),
    path('actualizar-experiencias/<int:pk>/', Update_experiencias.as_view(), name = 'actualizar-experiencias')
]