from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from .models import Jugadors
from django.contrib import messages

def register_view(request):
    if request.method == "POST":

        email = request.POST.get("email")
        nombre = request.POST.get("nombre")
        idioma = request.POST.get("idioma")
        privacidad = request.POST.get("privacidadRanking")

        # Validar duplicados
        if Jugadors.objects.filter(email=email).exists():
            messages.error(request, "Este correo ya está registrado")
            return render(request, "register.html")

        # Checkbox → booleano
        privacidad_bool = True if privacidad == "on" else False

        Jugadors.objects.create(
            email=email,
            nombre=nombre,
            idioma=idioma,
            privacidadRanking=privacidad_bool,
        )

        return redirect("sesion")  # Ruta del login

    return render(request, "register.html")

