from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth import login, authenticate
from django.shortcuts import render
from django.urls import reverse
from pettiApp import forms, models


def index(request):
    return render(request, 'index.html')

def busqueda_servicios(request):
    partners = models.User.objects.filter(is_partner=True)
    print('partners:', partners)
    context = {
        'partners': partners,
    }
    return render(request, 'busquedaServicios.html', context)

def inicio_sesion_admin(request):
    return render(request, 'inicioSesionAdmin.html')

def perfil_usuario(request):
    return render(request, 'perfilUsuario.html')

def registro_usuarios(request):
    return render(request, 'registroUsuarios.html')

def signup(request):
    if request.method == 'GET':
        form = forms.SignupForm()
        context = {
            'form': form
        }
        return render(request, 'registroUsuarios.html', context)
    elif request.method == 'POST':
        print('data:')
        print(request.POST)
        form = forms.SignupForm(request.POST)
        if form.is_valid():
            print('form is valid')
            cleaned_data = form.cleaned_data
            print('cleaned data:')
            print(cleaned_data)
            user = form.save()
            print('user:', user)
            email = form.cleaned_data.get('email')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(
                username=email,
                password=raw_password
            )
            login(request, user)
            return HttpResponseRedirect(reverse('pettiApp:index'))
        else:
            print('form is invalid')
            print(form.errors)
        context = {
            'form': form
        }
        return render(request, 'registroUsuarios.html', context)
    else:
        raise Exception('Invalid request method')

def mantenimiento(request):
    return render(request, 'mantenimiento.html')

def mantenimiento_servicios(request):
    return render(request, 'mantenimientoServicios.html')

def mantenimiento_usuarios(request):
    return render(request, 'mantenimientoUsuarios.html')

def perfil_partner(request):
    return render(request, 'perfilPartner.html')
 