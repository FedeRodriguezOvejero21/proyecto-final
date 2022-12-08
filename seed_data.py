from ejemplo.models import Familiar
Familiar(nombre="Federico", direccion="Avenida la Plata 486", numero_pasaporte=123123, fecha_nacimiento="21/07/1992").save()
Familiar(nombre="Maria", direccion="Cardoso 6", numero_pasaporte=890890, fecha_nacimiento="16/08/1956").save()
Familiar(nombre="Horacio", direccion="Avenida Rivadavia 8521", numero_pasaporte=345345, fecha_nacimiento="10/10/1955").save()
Familiar(nombre="Rosa", direccion="Avenida Rivadavia 8521", numero_pasaporte=567567, fecha_nacimiento="25/11/1920").save()
print("Se cargo con éxito los usuarios de pruebas")