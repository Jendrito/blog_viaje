from django.contrib import admin
from django.urls import path, include
from base.views import inicio
from base.views import login , search_experiencias_view
from django.views.generic.base import TemplateView 


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('contacto.urls')),
    path('', include('experiencias.urls')),
    path('', include('tramites.urls')),
    path('', TemplateView.as_view(template_name='inicio.html'), name='inicio'),
    path('', include("cuenta.urls")),
    path('', include("django.contrib.auth.urls")),
    path("login/", login, name = 'login'),
    path('search_experiencias_view/', search_experiencias_view, name='search'),
]