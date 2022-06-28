from multiprocessing import context
from urllib import request
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from .models import User
from .forms import  User_registration_form
from django.views.generic import  DetailView, DeleteView, UpdateView
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
# Create your views here.



def register(request):
    if request.method == 'POST':
        form = User_registration_form(request.POST)

        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username = username, password = password)
            login(request, user)
            context = {'message':f'Usuario creado correctamente, bienvenido {username}'}
            return render(request, 'inicio.html', context = context)
        else:
            errors = form.errors
            form = User_registration_form()
            context = {'errors':errors, 'form':form}
            return render(request, 'registration/signup.html', context = context)
    else:
        form = User_registration_form()
        context = {'form':form}
        return render(request, 'registration/signup.html', context =context)

@csrf_exempt
def login_vista(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data = request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request , user)
                return render(request, 'inicio.html')
            else:
                context = {'errors':'No hay ningun usuario con esas credenciales!!!'}
                form = AuthenticationForm()
                return render(request, 'registration/login.html', context = context)
        else:
            errors = form.errors
            form = AuthenticationForm()
            context = {'errors':errors, 'form':form} 
            return render(request, 'registration/login.html', context = context)
    else:
        form = AuthenticationForm()
        context = {'form':form}
        return render(request, 'registration/login.html', context = context)


def logout_vista(request):
    logout(request)
    return redirect('inicio')

class editarPerfil(UpdateView):
    model = User
    template_name = 'editar_perfil.html'
    fields = 'username', 'email', 'redes_sociales', 'descripcion','telefono','image'


    def get_success_url(self):
        return reverse('Perfil', kwargs = {'pk':self.object.pk})


            
class Perfil(DetailView):
    model = User
    template_name= 'perfil.html'
    def get_success_url(self):
        return reverse('Perfil', kwargs = {'pk':self.object.pk})