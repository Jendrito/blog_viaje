from dataclasses import Field
from distutils.command.upload import upload
from multiprocessing.sharedctypes import Value
from tkinter import Label
from django import forms
from .models import User_profile
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserEditForm(UserCreationForm):
    username = forms.CharField(label='Usuario')
    email = forms.EmailField(label='Modificar tu email')
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repita su contraseña', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        help_texts = {k:'' for k in fields}

