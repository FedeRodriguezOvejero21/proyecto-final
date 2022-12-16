from django.shortcuts import render, get_object_or_404
from ejemplo.models import Familiar
from ejemplo.forms import Buscar, FamiliarForm
from ejemplo.models import Automovil
from ejemplo.forms import Buscar, AutomovilForm
from ejemplo.models import Mascota
from ejemplo.forms import Buscar, MascotaForm
from django.views import View
from django.views.generic import ListView, CreateView, DeleteView, UpdateView

def index(request):
    return render(request, "ejemplo/saludar.html")


def saludar_a(request, nombre):
    return render(request,
    "ejemplo/saludar_a.html",
    {"nombre":nombre}
    )


def sumar(request, a, b):
    return render(request,
    "ejemplo/sumar.html",
    {"a":a,
     "b":b,
     "resultado":a + b
    }
    )

def buscar(request):
    lista_de_nombre=["Federico","Horacio","Maria","Francisco"]
    query = request.GET["q"]
    if query in lista_de_nombre:
        indice_de_resultado= lista_de_nombre.index(query)
        resultado=lista_de_nombre[indice_de_resultado]
    else:
        resultado= "No hay match"
    return render(request, "ejemplo/buscar.html", {"resultado":resultado})


def mostrar_familiares(request):
    lista_familiares = Familiar.objects.all()
    return render(request, "ejemplo/familiares.html", {"lista_familiares": lista_familiares})

class BuscarFamiliar(View):
    form_class = Buscar
    template_name = 'ejemplo/buscar.html'
    initial = {"nombre":""}

    def get(self, request):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form':form})
    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            nombre = form.cleaned_data.get("nombre")
            lista_familiares = Familiar.objects.filter(nombre__icontains=nombre).all() 
            form = self.form_class(initial=self.initial)
            return render(request, self.template_name, {'form':form, 
                                                        'lista_familiares':lista_familiares})
        return render(request, self.template_name, {"form": form})

class AltaFamiliar(View):

    form_class = FamiliarForm
    template_name = 'ejemplo/alta_familiar.html'
    initial = {"nombre":"", "direccion":"", "numero_pasaporte":"","fecha_nacimiento":""}

    def get(self, request):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form':form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            msg_exito = f"Se cargo con éxito el familiar {form.cleaned_data.get('nombre')}"
            form = self.form_class(initial=self.initial)
            return render(request, self.template_name, {'form':form, 
                                                        'msg_exito': msg_exito})
        
        return render(request, self.template_name, {"form": form})
 

class ActualizarFamiliar(View):

    form_class = FamiliarForm
    template_name = 'ejemplo/actualizar_familiar.html'
    initial = {"nombre":"", "direccion":"", "numero_pasaporte":"","fecha_nacimiento":""}
  
  
    def get(self, request, pk): 
        familiar = get_object_or_404(Familiar, pk=pk)
        form = self.form_class(instance=familiar)
        return render(request, self.template_name, {'form':form,'familiar': familiar})

    
    def post(self, request, pk): 
        familiar = get_object_or_404(Familiar, pk=pk)
        form = self.form_class(request.POST ,instance=familiar)
        if form.is_valid():
            form.save()
            msg_exito = f"Se actualizó con éxito el familiar {form.cleaned_data.get('nombre')}"
            form = self.form_class(initial=self.initial)
            return render(request, self.template_name, {'form':form, 
                                                        'familiar': familiar,
                                                        'msg_exito': msg_exito})
        
        return render(request, self.template_name, {"form": form}) 


class BorrarFamiliar(View):

    template_name = 'ejemplo/familiares.html'

    def get(self, request, pk): 
        familiar = get_object_or_404(Familiar, pk=pk)
        familiar.delete()
        familiar= Familiar.objects.all()
        return render(request, self.template_name, {'lista_familiares': familiar})

#metodo de ABM simplificado

class FamiliarList(ListView):
    model = Familiar

class FamiliarCrear(CreateView):
    model = Familiar
    success_url = "/panel-familia"
    fields = ["nombre", "direccion", "numero_pasaporte","fecha_nacimiento"]

class FamiliarBorrar(DeleteView):
    model = Familiar
    success_url = "/panel-familia"

class FamiliarActualizar(UpdateView):
    model = Familiar
    success_url = "/success_updated_message"
    fields = ["nombre", "direccion", "numero_pasaporte", "fecha_nacimiento"]

#automovil

class AutomovilList(ListView):
    model = Automovil

class AutomovilCrear(CreateView):
    model = Automovil
    success_url = "/panel-automovil"
    fields = ["marca", "modelo", "color","cantidad_de_puertas", "fecha_patentamiento"]

class AutomovilBorrar(DeleteView):
    model = Automovil
    success_url = "/panel-automovil"

class AutomovilActualizar(UpdateView):
    model = Automovil
    success_url = "/success_updated_message"
    fields = ["marca", "modelo", "color","cantidad_de_puertas", "fecha_patentamiento"]

#mascota

class MascotaList(ListView):
    model = Mascota

class MascotaCrear(CreateView):
    model = Mascota
    success_url = "/panel-mascota"
    fields = ["nombre", "animal", "edad", "fecha_adopcion"]

class MascotaBorrar(DeleteView):
    model = Mascota
    success_url = "/panel-mascota"

class MascotaActualizar(UpdateView):
    model = Mascota
    success_url = "/success_updated_message"
    fields = ["nombre", "animal", "edad", "fecha_adopcion"]