
from django.urls import path, include
from .views import editarPerfil, logout_vista, register, login_vista, editarPerfil, Perfil

urlpatterns = [
    path("registro/", register  , name="registro"),
    path("login/", login_vista , name="login"),
    path("logout/", logout_vista  , name="logout"),
    path("Perfil/<int:pk>/",Perfil.as_view() , name="Perfil"),
    path("editarPerfil/<int:pk>/", editarPerfil.as_view() , name="editarPerfil"),
]