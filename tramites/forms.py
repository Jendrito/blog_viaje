from django import forms
from tramites.models import Tramites

   
class Tramites_form(forms.ModelForm):
    class Meta:
        model = Tramites
        fields = [ 'nombre_tramites','pais','descripcion','image']

