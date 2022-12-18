Entrega intermedia del Proyecto final

Pasos a seguir:

1-abrir VSC code
2-usar clone git repository y agregar la url del proyecto compartido
3-crear o elegir una carpeta para el programa
4-abrir una terminal en VSC y python manange.py migrate (python3 si es mac) luego ejecutar python manage.py runserver para correr el programa
5-copiar la url que devuelve el programa que comienza con http:// y pegarla en el buscador
6-para importar algunos datos bases ejecutar el comando python shell y luego tipear import seed_data (aca hay un error en la fecha formato)

Aca tenemos 3 modelos: mi-familia (se carga con ls datos del seed_data), mis-automoviles, mis-mascotas

Las url sirven de base para crear nuevos datos en cada base,
http://127.0.0.1:8000/mi-familia/alta
http://127.0.0.1:8000/mis-mascotas/alta
http://127.0.0.1:8000/mis-automoviles/alta

Full path de todas las funciones son como debajo (aun no totalmente testeadas)

mi-familia/
mi-familia/buscar
mi-familia/alta
mi-familia/actualizar/<int:pk>
mi-familia/borrar/<int:pk>
mis-automoviles/
mis-automoviles/buscar
mis-automoviles/alta
mis-automoviles/actualizar/<int:pk>
mis-automoviles/borrar/<int:pk>
mis-mascotas/
mis-mascotas/buscar
mis-mascotas/alta
mis-mascotas/actualizar/<int:pk>
mis-mascotas/borrar/<int:pk>

Gracias,