from django.shortcuts import render
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic.list import ListView


from inicio.models import Vehiculos


def inicio(request): 
    return render(request, "inicio/inicio.html")



def acercademi(request): 
    return render(request, "inicio/acercademi.html")



class VehiculosListView(ListView):
    model = Vehiculos
    template_name = "inicio/lista_vehiculos.html"
    

class VehiculosDetailView(DetailView):
        model = Vehiculos
        template_name = "inicio/detalle_del_vehiculo.html"
    

class VehiculosCreateView(CreateView):
    model = Vehiculos
    template_name = "inicio/agregar_vehiculo.html"
    fields = ["modelo", "marca","color", "fecha_de_ingreso", "descripcion"]
    success_url = "/vehiculos/"


class VehiculosUpdateView(UpdateView):
    model = Vehiculos
    template_name = "inicio/modificar_caracteristicas.html"
    fields = ["modelo", "marca","color", "fecha_de_ingreso", "descripcion"]
    success_url = "/vehiculos/"


class VehiculosDeleteView(DeleteView):
    model = Vehiculos
    template_name = "inicio/eliminar_vehiculo.html"
    success_url = "/vehiculos/"

