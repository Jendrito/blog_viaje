from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import User_registration_form
from .models import User
from django.views.generic import  DetailView, DeleteView, UpdateView
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
# Create your views here.

@csrf_exempt
def register(request):
    if request.method == 'POST':
        form = User_registration_form(request.POST)

        if form.is_valid():
            form.save()
            user = form.save()
            login(request, user, backend='django.contrib.auth.backends.ModelBackend')
            context = {'message':f'Usuario creado correctamente, bienvenido {User.username}'}
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

class Update_perfil(UpdateView):
    model = User
    template_name = 'update_perfil.html'
    fields = '_all_'


    def get_success_url(self):
        return reverse('perfil', kwargs = {'pk':self.object.pk})