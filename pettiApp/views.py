from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')

def administracion(request):
    return render(request, 'administracion.html')

def busqueda_servicios(request):
    return render(request, 'busquedaServicios.html')

def inicio_sesion_admin(request):
    return render(request, 'inicioSesionAdmin.html')

def inicio_sesion_usuario(request):
    return render(request, 'inicioSesionUsuario.html')

def perfil_usuario(request):
    return render(request, 'perfilUsuario.html')

def registro_usuarios(request):
    return render(request, 'registroUsuarios.html')
