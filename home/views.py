from django.shortcuts import render

def index(request):
    return render(request, "index.html", {})

def Web_view(request):
    return render(request, 'game.html',{})

def challenges_view(request):
    return render(request, 'challenges.html',{})

def resources_view(request):
    return render(request, 'resources.html',{})

def solutions_view(request):
    return render(request, 'solutions.html',{})

def takeaction_view(request):
    return render(request, 'take-action.html',{})

#css
def baseStyle_view(request):
    return render(request, 'static/styles/baseStyle.css',{})
def layoutStyle_view(request):
    return render(request, 'static/styles/layout.css',{})
def resourcesStyle_view(request):
    return render(request, 'static/styles/resources.css',{})

#Inicio de sesion y registro
def login_view(request):
    return render(request, 'login.html',{})

def register_view(request):
    return render(request, 'register.html',{})

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

def login_view(request):
    if request.method == "POST":
        user = authenticate(
            request,
            username=request.POST["username"],
            password=request.POST["password"]
        )
        if user:
            login(request, user)
            return redirect('/')
        else:
            return render(request, "login.html", {"error": "Credenciales inválidas"})

    return render(request, "login.html")


def register_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]
        pass1 = request.POST["password1"]
        pass2 = request.POST["password2"]

        if pass1 != pass2:
            return render(request, "register.html", {"error": "Las contraseñas no coinciden"})

        User.objects.create_user(username=username, email=email, password=pass1)
        return redirect("/login/")

    return render(request, "register.html")

