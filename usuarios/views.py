from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login as web_login
from django.shortcuts import redirect
# Create your views here.


def login(request):
    
    if request.method == "POST":
        formulario = AuthenticationForm(request, data=request.POST)
        
        if formulario.is_valid():
            nombre_usuario = formulario.cleaned_data.get("username")
            contrasenia = formulario.cleaned_data.get("password")
            usuario =  authenticate(username=nombre_usuario, password=contrasenia)
            web_login(request, usuario)
            return redirect("inicio:inicio")
        else:
            return render(request, "usuarios/login.html", {"formulario":formulario})
    
    formulario = AuthenticationForm()
    return render(request, "usuarios/login.html", {"formulario":formulario})


