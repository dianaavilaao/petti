
from django.urls import include, path
from . import views
from django.contrib.auth import views as auth_views

app_name = 'pettiApp'

urlpatterns = [
    path('', views.index, name='index'), 
    path('index/', views.index, name='index'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('admin/', views.administracion, name='administracion'),  
    path('busqueda-servicios/', views.busqueda_servicios, name='busqueda_servicios'),  
    path('inicio-sesion-admin/', views.inicio_sesion_admin, name='inicio_sesion_admin'),  
    path('inicio-sesion-usuario/', views.inicio_sesion_usuario, name='inicio_sesion_usuario'),  
    path('perfil-usuario/', views.perfil_usuario, name='perfil_usuario'),  
    path('registro-usuarios/', views.registro_usuarios, name='registro_usuarios'),  
    path('mantenimiento/', views.mantenimiento, name='mantenimiento'),
    path('mantenimiento-servicios/', views.mantenimiento_servicios, name='mantenimiento_servicios'),
    path('mantenimiento-usuarios/', views.mantenimiento_usuarios, name='mantenimiento_usuarios'),
]
