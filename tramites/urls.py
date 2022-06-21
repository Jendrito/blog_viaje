from django.urls import path

from tramites.views import ver_tramites, crear_tramites, Update_tramites, Delete_tramites
urlpatterns =[
    path('ver-tramites/', ver_tramites, name = 'ver-tramites'),
    path('crear-tramites/', crear_tramites, name = 'crear-tramites'),
    path('borrar-tramites/<int:pk>/', Delete_tramites.as_view(), name = 'borrar-tramites'),
    path('actualizar-tramites/<int:pk>/', Update_tramites.as_view(), name = 'actualizar-tramites'),
]