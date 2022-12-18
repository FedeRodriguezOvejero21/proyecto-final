from django.db import models

class Familiar(models.Model):
    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=200)
    numero_pasaporte = models.IntegerField()
    fecha_nacimiento= models.DateField()
  
    def __str__(self):
      return f"{self.id}--{self.nombre}--{self.direccion}--{self.numero_pasaporte}--{self.fecha_nacimiento}"
    

class Dummy(models.Model):
    nombre=models.CharField(max_length=100)

#clase automovil

class Automovil(models.Model):
    marca = models.CharField(max_length=100)
    modelo = models.CharField(max_length=200)
    color = models.CharField(max_length=200)
    cantidad_de_puertas = models.IntegerField()
    fecha_patentamiento= models.DateField()
  
    def __str__(self):
      return f"{self.id}--{self.marca}--{self.modelo}--{self.color}--{self.cantidad_de_puertas}--{self.fecha_patentamiento}"


class Dummy(models.Model):
    nombre=models.CharField(max_length=100)

#clase mascota

class Mascota(models.Model):
    nombre = models.CharField(max_length=100)
    animal = models.CharField(max_length=200)
    edad = models.IntegerField()
    fecha_adopcion= models.DateField()
  
    def __str__(self):
      return f"{self.id}--{self.nombre}--{self.animal}--{self.edad}--{self.fecha_adopcion}"
    

class Dummy(models.Model):
    nombre=models.CharField(max_length=100)