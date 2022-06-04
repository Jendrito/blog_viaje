from django import forms

class ContactoForm(forms.Form):
    email = forms.EmailField(required=True)
    nombre = forms.CharField(required=True)
    mensaje = forms.CharField(widget=forms.Textarea, required=True)