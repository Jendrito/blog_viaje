from django.contrib import admin
from django.urls import path, include
from base.views import inicio

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('contacto.urls')),
    path('', include('experiencias.urls')),
    path('', include('tramites.urls')),
    path('', inicio, name = 'inicio')
]