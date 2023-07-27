import requests
from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import LoginForm, RegisterForm
from .models import userData

def homeView(request):
    return render(request, 'home.html', {'user': request.user})

def loginView(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            dni = form.cleaned_data.get('dni')
            password = form.cleaned_data.get('contraseña')
            user = userData.objects.authenticate_user(dni=dni, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})

def registerView(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            dni = form.cleaned_data['dni']
            nombres = form.cleaned_data['nombres']
            apellido_paterno = form.cleaned_data['apellido_paterno']
            apellido_materno = form.cleaned_data['apellido_materno']
            password = form.cleaned_data['contraseña'] 

            if validate_dni(dni, nombres, apellido_paterno, apellido_materno):
                userData.objects.create(dni=dni, nombres=nombres, apellido_paterno=apellido_paterno, apellido_materno=apellido_materno, password=password)
                return redirect('home')
            else:
                alert_message = "Los datos del DNI no coinciden con la API. Verifícalos e intenta nuevamente."
                return render(request, 'register.html', {'form': form, 'alert_message': alert_message})
    else:
        form = RegisterForm()
    return render(request, 'register.html', {'form': form})

def validate_dni(dni, nombres, apellido_paterno, apellido_materno):
    url = f'https://dniruc.apisperu.com/api/v1/dni/{dni}?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJlbWFpbCI6InJleXNlci56YXAuMTQ1QGdtYWlsLmNvbSJ9.e_VtxCOl5DDGy4tU32LZ8UwOCbidFwnEV24rn470pTw'
    response = requests.get(url)
    data = response.json()
    if data.get('success', False):
        api_nombres = data.get("nombres", "").upper().replace(" ", "")
        api_apellidos = (data.get("apellidoPaterno","") + data.get("apellidoMaterno","")).upper().replace(" ", "")
        return api_nombres == nombres.upper().replace(" ", "") and api_apellidos == (apellido_paterno + apellido_materno).upper().replace(" ", "")
    return False
