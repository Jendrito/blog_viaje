from django.urls import path

from experiencias.views import ver_experiencias, Create_experiencias, Delete_experiencias, Update_experiencias, Detail_experiencias

urlpatterns =[
    path('ver-experiencias/', ver_experiencias, name = 'ver-experiencias'),
    path('crear-experiencias/', Create_experiencias.as_view() , name = 'crear-experiencias'),
    path('detalle-experiencia/<int:pk>/', Detail_experiencias.as_view(), name = 'detalle-experiencia'),
    path('borrar-experiencias/<int:pk>/', Delete_experiencias.as_view(), name = 'borrar-experiencias'),
    path('actualizar-experiencias/<int:pk>/', Update_experiencias.as_view(), name = 'actualizar-experiencias')
]