from django import forms
from tramites.models import Tramites

class Tramites_form(forms.Form):
    nombre_tramites = forms.CharField(max_length=100)
    pais = forms.CharField(max_length=50)
    descripcion = forms.CharField(max_length=10000)
   


