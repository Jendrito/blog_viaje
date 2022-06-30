from multiprocessing.sharedctypes import Value
from django import forms
from .models import User
from django.contrib.auth.forms import UserCreationForm

class User_registration_form(UserCreationForm):
    email = forms.EmailField()
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repita su contraseña', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', ]
        help_texts = {k:'' for k in fields}

class Perfil(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'redes_sociales', 'descripcion','telefono','image' ]
        help_texts = {k:'' for k in fields}

        