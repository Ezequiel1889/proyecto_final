from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import authenticate, login as web_login
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from usuarios.models import InfoAvatar

from usuarios.forms import FormularioUsuario,EdicionPerfil
# Create your views here.


def login(request):
    
    if request.method == "POST":
        formulario = AuthenticationForm(request, data=request.POST)
        
        
        if formulario.is_valid():
            nombre_usuario = formulario.cleaned_data.get("username")
            contrasenia = formulario.cleaned_data.get("password")
            
            user =  authenticate(username=nombre_usuario, password=contrasenia)
            
            web_login(request, user)
            
            InfoAvatar.objects.get_or_create(user=user)
            
            return redirect("inicio:inicio")
        else:
            return render(request, "usuarios/login.html", {"formulario":formulario})
    
    formulario = AuthenticationForm()
    return render(request, "usuarios/login.html", {"formulario":formulario})


def registro(request):
    
    if request.method == "POST":
        
        formulario = FormularioUsuario(request.POST)
        
        if formulario.is_valid():
            formulario.save()
            return redirect("usuarios:login")
        else:
            return render(request, "usuarios/registro.html", {"formulario":formulario})
            
        
    formulario = FormularioUsuario()
    return render(request, "usuarios/registro.html", {"formulario":formulario})

@login_required
def editar_perfil(request): 
  if request.method == "POST":
        
        formulario = EdicionPerfil(request.POST,request.FILES, instance=request.user)
        
        if formulario.is_valid():
            
            if formulario.cleaned_data.get("avatar"):
             
               request.user.infoavatar.avatar = formulario.cleaned_data.get("avatar")
               request.user.infoavatar.save()
           
            formulario.save()
            
            
            return redirect("usuarios:editar_perfil")
        else:
            return render(request, "usuarios/editar_perfil.html", {"formulario":formulario})
            
        
  formulario = EdicionPerfil (initial={"avatar": request.user.infoavatar.avatar}, instance=request.user)
  return render(request, "usuarios/editar_perfil.html", {"formulario":formulario})



