Entrega intermedia del Proyecto final

Pasos a seguir:

1-abrir VSC code
2-usar clone git repository y agregar la url del proyecto compartido
3-crear o elegir una carpeta para el programa
4-abrir una terminal en VSC y python manange.py migrate (python3 si es mac) luego ejecutar python manage.py runserver para correr el programa
5-copiar la url que devuelve el programa que comienza con http:// y pegarla en el buscador
6-para importar algunos datos bases ejecutar el comando python shell y luego tipear import seed_data (aca hay un error en la fecha formato)

Aca tenemos 3 modelos: mi-familia (se carga con ls datos del seed_data), panel-automovil, panel-mascota

Las url sirven de base para crear nuevos datos en cada base,
http://127.0.0.1:8000/mi-familia/alta
http://127.0.0.1:8000/panel-mascota/crear
http://127.0.0.1:8000/panel-automovil/crear

Full path de todas las funciones son como debajo (aun no totalmente testeadas)

mi-familia/
mi-familia/buscar
mi-familia/alta
mi-familia/actualizar/<int:pk>
mi-familia/borrar/<int:pk>
panel-familia/
panel-familia/crear
panel-familia/<int:pk>/borrar
panel-familia/<int:pk>/actualizar
panel-mascota/
panel-mascota/crear
panel-mascota/<int:pk>/borrar
panel-mascota/<int:pk>/actualizar
panel-automovil/
panel-automovil/crear
panel-automovil/<int:pk>/borrar
panel-automovil/<int:pk>/actualizar

Gracias,