from django.contrib import admin
from django.urls import path, include
from .views import logout_vista, register, login_vista, editarPerfil

urlpatterns = [
    path("registro/", register  , name="registro"),
    path("login/", login_vista , name="login"),
    path("logout/", logout_vista  , name="logout"),
    path("editarPerfil/", editarPerfil , name="editarPerfil"),
]