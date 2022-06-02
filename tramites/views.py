from django.shortcuts import render
from tramites.models import Tramites

def ver_tramites(request):
    tramites = Tramites.objects.all()
    context = {'tramites':tramites}
    return render(request, 'tramites.html', context=context)

#def crear_tramites(request):