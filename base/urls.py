from django.contrib import admin
from django.urls import path, include
from base.views import inicio
from base.views import login , search_experiencias_view, nosotros, esteban,demian, carolina
from django.views.generic.base import TemplateView 
from django.conf import settings
from django.conf.urls.static import static

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
    path('nosotros/', nosotros , name='nosotros'),
    path('esteban/', esteban , name='esteban'),
    path('demian/', demian , name='demian'),
    path('carolina/', carolina , name='carolina'),
    

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)