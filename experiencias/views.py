from django.shortcuts import render
from experiencias.models import Experiencias

def ver_experiencias(request):
    experiencias = Experiencias.objects.all()
    context = {'experiencias':experiencias}
    return render(request, 'experiencias.html', context=context)
   
#def crear_experiencias(request):