from django.shortcuts import render, redirect
from tramites.models import Tramites
from .forms import Tramites_form
from django.views.generic import  DetailView,  DeleteView, UpdateView
from django.urls import reverse

def ver_tramites(request):
    tramites = Tramites.objects.all()
    context = {'tramites':tramites}
    return render(request, 'ver_tramites.html', context=context)

def crear_tramites(request):
    if request.method == 'GET':
        form = Tramites_form()
        context = {'form':form}
        return render(request, 'crear_tramites.html', context=context)
    else:
        form = Tramites_form(request.POST)
        if form.is_valid():
            new_tramite = Tramites.objects.create(
                nombre_tramites = form.cleaned_data['nombre_tramites'],
                pais = form.cleaned_data['pais'],
                descripcion = form.cleaned_data['descripcion'],
            )
            context ={'new_tramite':new_tramite}
        return redirect('/ver-tramites')


class Delete_tramites(DeleteView):
    model = Tramites
    template_name = "borrar_tramites.html"

    def get_success_url(self):
        return reverse('ver-tramites')

class Update_tramites(UpdateView):
    model = Tramites
    template_name = 'actualizar_tramites.html'
    fields = 'nombre_tramites', 'pais', 'descripcion'

    def get_success_url(self):
        return reverse('ver-tramites', kwargs = {'pk':self.object.pk})
