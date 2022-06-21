from distutils.command.upload import upload
from multiprocessing.sharedctypes import Value
from tkinter import Label
from django import forms
from .models import User
from django.contrib.auth.forms import UserCreationForm

class User_registration_form(forms.ModelForm):
    password = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repita su contraseña', widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'password2', 'imagen', 'telefono', 'redes_sociales']
        help_texts = {k:'' for k in fields}