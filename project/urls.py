"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView
from ejemplo.views import (index, saludar_a, sumar,
                           buscar, mostrar_familiares,BuscarFamiliar,
                           AltaFamiliar,ActualizarFamiliar,BorrarFamiliar,
                           FamiliarList,FamiliarCrear,FamiliarBorrar,FamiliarActualizar,FamiliarDetalle)
from ejemplo.views import (index,
                           mostrar_automoviles,BuscarAutomovil, AltaAutomovil, ActualizarAutomovil, BorrarAutomovil)
from ejemplo.views import (index,
                           mostrar_mascotas,BuscarMascotas, AltaMascotas, ActualizarMascotas, BorrarMascotas)
from Entrega_Final_FRO.views import (index, PostDetalle, PostListar, 
                                PostCrear, PostBorrar, PostActualizar,
                                UserSignUp,UserLogin, UserLogout,
                                AvatarActualizar,UserActualizar,MensajeCrear,MensajeListar,MensajeDetalle)
from django.contrib.admin.views.decorators import staff_member_required

urlpatterns = [
    path('admin/', admin.site.urls),
    #path("saludar/", index),
    #path("saludar-a/<nombre>/", saludar_a),
    #path("sumar/<int:a>/<int:b>/", sumar),
    #path("buscar/", buscar),
    path("mi-familia/", mostrar_familiares),
    path("mi-familia/buscar", BuscarFamiliar.as_view()),
    path("mi-familia/alta", AltaFamiliar.as_view()),
    path('mi-familia/actualizar/<int:pk>', ActualizarFamiliar.as_view()),
    path('mi-familia/borrar/<int:pk>', BorrarFamiliar.as_view()),
    #path('panel-familia/', FamiliarList.as_view()),
    #path('panel-familia/crear', FamiliarCrear.as_view()),
    #path('panel-familia/<int:pk>/borrar', FamiliarBorrar.as_view()),
    #path('panel-familia/<int:pk>/actualizar', FamiliarActualizar.as_view()),
    #path("panel-familia"/<int:pk>/detalle",FamiliaDetalle.as.view())
    path('panel-familia/<int:pk>/detalle', FamiliarDetalle.as_view()),
    path('success_updated_message/', TemplateView.as_view(template_name="ejemplo/success_updated_message.html")),
    
    #Automovil
    path("mis-automoviles/", mostrar_automoviles),
    path("mis-automoviles/buscar", BuscarAutomovil.as_view()),
    path("mis-automoviles/alta", AltaAutomovil.as_view()),
    path('mis-automoviles/actualizar/<int:pk>', ActualizarAutomovil.as_view()),
    path('mis-automoviles/borrar/<int:pk>', BorrarAutomovil.as_view()),
    #path('panel-automovil/', AutomovilList.as_view()),
    #path('panel-automovil/crear', AutomovilCrear.as_view()),
    #path('panel-automovil/<int:pk>/borrar', AutomovilBorrar.as_view()),
    #path('panel-automovil/<int:pk>/actualizar', AutomovilActualizar.as_view()),

    #Mascota
    path("mis-mascotas/", mostrar_mascotas),
    path("mis-mascotas/buscar", BuscarMascotas.as_view()),
    path("mis-mascotas/alta", AltaMascotas.as_view()),
    path('mis-mascotas/actualizar/<int:pk>', ActualizarMascotas.as_view()),
    path('mis-mascotas/borrar/<int:pk>', BorrarMascotas.as_view()),
    #path('panel-mascota/', MascotaList.as_view()),
    #path('panel-mascota/crear', MascotaCrear.as_view()),
    #path('panel-mascota/<int:pk>/borrar', MascotaBorrar.as_view()),
    #path('panel-mascota/<int:pk>/actualizar', MascotaActualizar.as_view()),

    #ejemplo dos clase 141222
    path("Entrega-Final-FRO/", index, name="Entrega-Final-FRO-index"),
    path("Entrega-Final-FRO/<int:pk>/detalle/", PostDetalle.as_view(),name="Entrega-Final-FRO-detalle"),
    path("Entrega-Final-FRO/listar/", PostListar.as_view(),name="Entrega-Final-FRO-listar"),
    path("Entrega-Final-FRO/crear/", PostCrear.as_view(),name="Entrega-Final-FRO-crear"),
    path("Entrega-Final-FRO/<int:pk>/borrar/",PostBorrar.as_view(),name="Entrega-Final-FRO-borrar"),
    path("Entrega-Final-FRO/<int:pk>/actualizar/", PostActualizar.as_view(),name="Entrega-Final-FRO-actualizar"),
    path("Entrega-Final-FRO/signup/", UserSignUp.as_view(),name="Entrega-Final-FRO-signup"),
    path("Entrega-Final-FRO/login/", UserLogin.as_view(),name="Entrega-Final-FRO-login"),
    path("Entrega-Final-FRO/logout/", UserLogout.as_view(),name="Entrega-Final-FRO-logout"),
    path("Entrega-Final-FRO/avatars/<int:pk>/actualizar/",AvatarActualizar.as_view(), name="Entrega-Final-FRO-avatars-actualizar"),
    path("Entrega-Final-FRO/users/<int:pk>/actualizar/",UserActualizar.as_view(), name="Entrega-Final-FRO-users-actualizar"),
    path("Entrega-Final-FRO/mensajes/crear/", MensajeCrear.as_view(), name="Entrega-Final-FRO-mensajes-crear"),
    path("Entrega-Final-FRO/mensajes/<int:pk>/detalle/", MensajeDetalle.as_view(), name="Entrega-Final-FRO-mensajes-detalle"),
    path("Entrega-Final-FRO/mensajes/listar/", MensajeListar.as_view(), name="Entrega-Final-FRO-mensajes-listar"),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)