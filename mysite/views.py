# views.py
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # Redirigir al usuario a una página de inicio o a donde desees
            return redirect('home')
        else:
            # Mensaje de error si el usuario no existe o la contraseña es incorrecta
            return render(request, 'login.html', {'error_message': 'Usuario o contraseña incorrectos'})
    else:
        return render(request, 'login.html')
