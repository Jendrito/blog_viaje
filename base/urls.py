from django.contrib import admin
from django.urls import path, include
from base.views import inicio
from base.views import login
from django.views.generic.base import TemplateView # new


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('contacto.urls')),
    path('', include('experiencias.urls')),
    path('', include('tramites.urls')),
    path('', TemplateView.as_view(template_name='inicio.html'), name='inicio'),
    path('', include("cuenta.urls")),
    path('', include("django.contrib.auth.urls")),
    path("login/", login, name = 'login'),
]