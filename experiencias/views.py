from urllib import request
from django.shortcuts import render, redirect
from experiencias.models import Experiencias
from experiencias.forms import Experiencias_form
from django.urls import reverse
from django.views.generic import  DetailView,  DeleteView, UpdateView, CreateView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin


def ver_experiencias(request):
    experiencias = Experiencias.objects.all()
    context = {'experiencias':experiencias}
    return render(request, 'experiencias/ver_experiencias.html', context=context)
   
class Create_experiencias(CreateView, LoginRequiredMixin):
    model = Experiencias
    template_name = 'experiencias/crear_experiencia.html'
    fields = '__all__'

    def get_success_url(self):
        return reverse('detalle-experiencia', kwargs={'pk':self.object.pk})

class Detail_experiencias(DetailView, LoginRequiredMixin):
    model = Experiencias
    template_name= 'experiencias/detalle_experiencia.html'

class Delete_experiencias(DeleteView, LoginRequiredMixin):
    model = Experiencias
    template_name = "experiencias/borrar_experiencias.html"

    def get_success_url(self):
        return reverse('ver-experiencias')

class Update_experiencias(UpdateView, LoginRequiredMixin):
    model = Experiencias
    template_name = 'experiencias/actualizar_experiencias.html'
    fields = 'titulo', 'pais', 'cuerpo', 'fecha', 'autor', 'image'


    def get_success_url(self):
        return reverse('detalle-experiencia', kwargs = {'pk':self.object.pk})
    
