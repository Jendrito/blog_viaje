from django.shortcuts import render, redirect
from tramites.models import Tramites
from .forms import Tramites_form
from django.views.generic import  DetailView,  DeleteView, UpdateView, CreateView
from django.urls import reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

def ver_tramites(request):
    tramites = Tramites.objects.all()
    context = {'tramites':tramites}
    return render(request, 'tramites/ver_tramites.html', context=context)

class Create_tramites(CreateView, LoginRequiredMixin):
    model = Tramites
    template_name = 'tramites/crear_tramites.html'
    fields =  '__all__'

    def get_success_url(self):
        return reverse('detalle-tramite', kwargs={'pk':self.object.pk})


class Detail_tramite(DetailView, LoginRequiredMixin):
    model = Tramites
    template_name= 'tramites/detalle_tramite.html'

class Delete_tramites(DeleteView, LoginRequiredMixin):
    model = Tramites
    template_name = "tramites/borrar_tramites.html"

    def get_success_url(self):
        return reverse('ver-tramites')

class Update_tramites(UpdateView, LoginRequiredMixin):
    model = Tramites
    template_name = 'tramites/actualizar_tramites.html'
    fields = 'nombre_tramites','pais', 'fecha', 'descripcion','image'

    def get_success_url(self):
        return reverse('detalle-tramite', kwargs = {'pk':self.object.pk})
