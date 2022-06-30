from multiprocessing import context
from django.shortcuts import render
from experiencias.models import Experiencias
from tramites.models import Tramites

def inicio(request):
    return render(request, 'inicio.html')

def demian(request):
    return render(request, 'nosotros/demian.html')

def esteban(request):
    return render(request, 'nosotros/esteban.html')

def carolina(request):
    return render(request, 'nosotros/carolina.html')

def login(request):
    return render(request, 'registration/login.html')

def search_experiencias_view(request):
    print(request.GET)
    experiencias = Experiencias.objects.filter(pais__contains = request.GET['search'])
    tramites = Tramites.objects.filter( pais__contains= request.GET['search'])
    context = {'experiencias':experiencias, 'tramites':tramites}

    return render(request, 'buscador/search_experiencias.html', context = context)

def nosotros(request):
    context={nosotros:'nosotros'}
    return render(request, 'nosotros/nosotros.html', context = context)