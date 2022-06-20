from django.db import models
from django.views.generic import  DetailView,  DeleteView, UpdateView
from django.urls import reverse

class Tramites(models.Model):
    nombre_tramites = models.CharField(max_length=100)
    pais = models.CharField(max_length=20)
    descripcion = models.CharField(max_length=5000)
    class Meta:
        verbose_name = 'Tramites'
        verbose_name_plural = 'Tramites'

    def _str_(self):
        return self.nombre_tramites

class Delete_tramites(DeleteView):
    model = Tramites
    template_name = "borrar_tramites.html"

    def get_success_url(self):
        return reverse('ver_tramites')

class Update_tramites(UpdateView):
    model = Tramites
    template_name = 'actualizar_tramites.html'
    fields = '_all_'

    def get_success_url(self):
        return reverse('ver_tramites', kwargs = {'pk':self.object.pk})