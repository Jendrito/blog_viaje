from django.shortcuts import render, redirect
from tramites.models import Tramites
from .forms import Tramites_form

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



