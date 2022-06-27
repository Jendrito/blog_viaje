from multiprocessing import context
from django.shortcuts import render
from experiencias.models import Experiencias
from tramites.models import Tramites

def inicio(request):
    return render(request, 'inicio.html')


def login(request):
    return render(request, 'login.html')

def search_experiencias_view(request):
    print(request.GET)
    experiencias = Experiencias.objects.filter(pais__contains = request.GET['search'])
    tramites = Tramites.objects.filter( pais__contains= request.GET['search'])
    context = {'experiencias':experiencias, 'tramites':tramites}

    return render(request, 'search_experiencias.html', context = context)

def nosotros(request):
    context={nosotros:'nosotros'}
    return render(request, 'nosotros.html', context = context)