from django.urls import path 
from inicio import views 


app_name= "inicio"

urlpatterns = [
    
    path("", views.inicio, name="inicio"),
    path("acerca-de-mi/", views.acercademi, name="acercademi"),
    path("vehiculos/", views.VehiculosListView.as_view(), name="lista_vehiculos"),
    path("vehiculos/agregar/", views.VehiculosCreateView.as_view(), name="agregar_vehiculo"),
    path("vehiculos/<int:pk>", views.VehiculosDetailView.as_view(), name="detalle_del_vehiculo"),
    path("vehiculos/<int:pk>/modificar/", views.VehiculosUpdateView.as_view(), name="modificar_caracteristicas"),
    path("vehiculos/<int:pk>/eliminar/", views.VehiculosDeleteView.as_view(), name="eliminar_vehiculo"),
    
    
    
]