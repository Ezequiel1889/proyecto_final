from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.


class Vehiculos(models.Model):
   modelo=models.CharField(max_length=40)
   marca=models.CharField(max_length=30)
   color=models.CharField(max_length=20)
   fecha_de_ingreso= models.DateField()
   descripcion=RichTextField()
   
   
   def __str__(self):
    return f"{self.marca} - {self.modelo}"