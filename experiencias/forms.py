from django import forms
from .models import Experiencias

class Experiencias_form(forms.ModelForm):
    class Meta:
        model = Experiencias
        fields = [ 'titulo','pais','fecha','autor','cuerpo','image']
        