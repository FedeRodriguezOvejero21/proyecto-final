from django.db import models


class Familiar(models.Model):
    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=200)
    numero_pasaporte = models.IntegerField()
    fecha_nacimiento= models.DateField()

    def __str__(self):
      return f"{self.nombre}, {self.numero_pasaporte}, {self.id}, {self.fecha_nacimiento}"
    

class Dummy(models.Model):
    nombre=models.CharField(max_length=100)
   
