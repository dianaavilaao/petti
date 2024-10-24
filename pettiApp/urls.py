
from django.urls import include, path
from . import views
from django.contrib.auth import views as auth_views

app_name = 'pettiApp'

urlpatterns = [
    path('', views.index, name='index'), 
    path('index/', views.index, name='index'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'), 
    path('busqueda-servicios/', views.busqueda_servicios, name='busqueda_servicios'),  
    path('inicio-sesion-admin/', views.inicio_sesion_admin, name='inicio_sesion_admin'),  
    path('perfil-usuario/', views.perfil_usuario, name='perfil_usuario'),  
    path('registro-usuarios/', views.registro_usuarios, name='registro_usuarios'),  
    path('mantenimiento/', views.mantenimiento, name='mantenimiento'),
    path('mantenimiento-servicios/', views.mantenimiento_servicios, name='mantenimiento_servicios'),
    path('mantenimiento-usuarios/', views.mantenimiento_usuarios, name='mantenimiento_usuarios'),
    path('perfil-partner/', views.perfil_partner, name='perfil_partner'),  
]

