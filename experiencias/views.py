from django.shortcuts import render, redirect
from experiencias.models import Experiencias
from experiencias.forms import Experiencias_form
from django.urls import reverse_lazy

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

