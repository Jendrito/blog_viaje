from django.shortcuts import render
from .forms import ContactoForm
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect


def contacto(request):
    if request.method == 'GET':
        form = ContactoForm()
    else:
        form = ContactoForm(request.POST)
        if form.is_valid():
            nombre = form.cleaned_data['nombre']
            email = form.cleaned_data['email']
            mensaje = form.cleaned_data['mensaje']
            try:
                send_mail(nombre, mensaje, email, ['Blog-Viajes@gmail.com'])
            except BadHeaderError:
                return HttpResponse('Error')
            return redirect('exitos')
    return render(request, "contacto/contacto.html", {'form': form})

def exitos(request):
    return render(request, 'contacto/exitos.html', )

    
