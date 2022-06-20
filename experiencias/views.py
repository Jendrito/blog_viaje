from django.shortcuts import render, redirect
from experiencias.models import Experiencias
from experiencias.forms import Experiencias_form
from django.urls import reverse
from django.views.generic import  DetailView,  DeleteView, UpdateView

def ver_experiencias(request):
    experiencias = Experiencias.objects.all()
    context = {'experiencias':experiencias}
    return render(request, 'ver_experiencias.html', context=context)
   
#def crear_experiencias(request):

def crear_experiencias(request):
    if request.method == 'GET':
        form = Experiencias_form()
        context = {'form':form}
        return render(request, 'crear_experiencia.html', context=context)
    else:
        form = Experiencias_form(request.POST)
        if form.is_valid():
            new_experiencia = Experiencias.objects.create(
                titulo = form.cleaned_data['titulo'],
                pais = form.cleaned_data['pais'],
                cuerpo = form.cleaned_data['cuerpo'],
                fecha = form.cleaned_data['fecha'],
                autor = form.cleaned_data['autor'],
            )
            context ={'new_experiencia':new_experiencia}
        return redirect('/ver-experiencias')

class Delete_experiencias(DeleteView):
    model = Experiencias
    template_name = "borrar_experiencias.html"

    def get_success_url(self):
        return reverse('ver_experiencias')

class Update_experiencias(UpdateView):
    model = Experiencias
    template_name = 'actualizar_experiencias.html'
    fields = '_all_'


    def get_success_url(self):
        return reverse('ver_experiencias', kwargs = {'pk':self.object.pk})