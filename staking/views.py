from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages

def custom_login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)  # Verifica credenciales
        if user is not None:
            login(request, user)  # Inicia sesión
            return redirect('account-list')  # Redirige al usuario después del login
        else:
            messages.error(request, "Usuario o contraseña incorrectos")  # Muestra error

    return render(request, 'login.html')