from ejemplo.models import Familiar
from ejemplo.models import Automovil
from ejemplo.models import Mascota
Familiar(nombre="Federico", direccion="Avenida la Plata 486", numero_pasaporte=123123, fecha_nacimiento= "1992/07/21").save()
Familiar(nombre="Maria", direccion="Cardoso 6", numero_pasaporte=890890, fecha_nacimiento= "1955/08/16").save()
Familiar(nombre="Horacio", direccion="Avenida Rivadavia 8521", numero_pasaporte=345345, fecha_nacimiento= "1960/04/24").save()
Familiar(nombre="Rosa", direccion="Avenida Rivadavia 8521", numero_pasaporte=567567, fecha_nacimiento= "1920/03/21").save()
Automovil(marca="Fiat", modelo="Duna", color="Azul", cantidad_de_puertas= "4",fecha_patentamiento="1986/06/15").save()
Automovil(marca="Renault", modelo="Sandero", color="Blanco", cantidad_de_puertas= "5",fecha_patentamiento="2018/05/21").save()
Automovil(marca="Toyota", modelo="Etios", color="Rojo", cantidad_de_puertas= "3",fecha_patentamiento="2020/10/05").save()
Automovil(marca="Volkswagen", modelo="Golf", color="Negro", cantidad_de_puertas= "3",fecha_patentamiento="2014/07/19").save()
Mascota(nombre="Dragoon", animal="Gata", edad=15, fecha_adopcion= "2003/10/06").save()
Mascota(nombre="Dinka", animal="Perra", edad=17, fecha_adopcion= "1990/07/21").save()
Mascota(nombre="Goku", animal="Perro", edad=5, fecha_adopcion= "2004/05/16").save()
Mascota(nombre="Maia", animal="Perra", edad=3, fecha_adopcion= "2007/11/02").save()
print("Se cargo con éxito los usuarios de pruebas")