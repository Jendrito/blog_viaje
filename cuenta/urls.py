from django.contrib import admin
from django.urls import path, include
from .views import SignUpView
urlpatterns = [
    path("registro/",  SignUpView.as_view(), name="registro"),
]