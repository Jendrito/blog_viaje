from email.policy import default
from django import forms
from .models import Experiencias
from cuenta.models import User

class Experiencias_form(forms.ModelForm):
    class Meta:
        model = Experiencias
        fields = [ 'titulo','pais','fecha','autor','cuerpo','image']
        