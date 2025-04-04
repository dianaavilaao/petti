from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth import login, authenticate
from django.shortcuts import render
from django.urls import reverse
from pettiApp import forms, models
import requests

def index(request):
    weather_data = get_weather_data("Santiago")
    context = {
        'weather': weather_data
    }
    return render(request, 'index.html', context)

def get_weather_data(city):
    api_key = "1a2c757e3bace7a48948bc12225ed37c"  
    base_url = "https://api.openweathermap.org/data/2.5/weather"
    
    try:
        params = {
            'q': city,
            'appid': api_key,
            'units': 'metric'  
        }
        
        response = requests.get(base_url, params=params)
        print(f"API Response Status: {response.status_code}")
        
        data = response.json()
        print(f"API Response Data: {data}")
        
        if response.status_code == 200:
            weather_info = {
                'city': data['name'],
                'temperature': round(data['main']['temp']),
                'description': data['weather'][0]['description'],
                'icon': data['weather'][0]['icon'],
                'humidity': data['main']['humidity'],
                'wind_speed': data['wind']['speed']
            }
            return weather_info
        else:
            print(f"Error en la API: {data.get('message', 'No hay mensaje de error')}")
            return {
                'city': city,
                'temperature': '--',
                'description': 'No disponible',
                'icon': '01d',  
                'humidity': '--',
                'wind_speed': '--'
            }
    except Exception as e:
        print(f"Error detallado al obtener datos del clima: {str(e)}")
        import traceback
        traceback.print_exc()
        return {
            'city': city,
            'temperature': '--',
            'description': 'No disponible',
            'icon': '01d',  
            'humidity': '--',
            'wind_speed': '--'
        }

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
 