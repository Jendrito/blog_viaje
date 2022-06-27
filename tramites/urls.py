from django.urls import path

from tramites.views import ver_tramites, Create_tramites, Update_tramites, Delete_tramites, Detail_tramite
urlpatterns =[
    path('ver-tramites/', ver_tramites, name = 'ver-tramites'),
    path('crear-tramites/',Create_tramites.as_view() , name = 'crear-tramites'),
    path('detalle-tramite/<int:pk>/', Detail_tramite.as_view(), name = 'detalle-tramite'),
    path('borrar-tramites/<int:pk>/', Delete_tramites.as_view(), name = 'borrar-tramites'),
    path('actualizar-tramites/<int:pk>/', Update_tramites.as_view(), name = 'actualizar-tramites'),
]