from django import forms

class Experiencias_form(forms.Form):
    titulo = forms.CharField(max_length=100)
    pais = forms.CharField(max_length=50)
    fecha = forms.DateTimeField()
    autor = forms.CharField(max_length=50)
    cuerpo = forms.CharField(max_length=10000)