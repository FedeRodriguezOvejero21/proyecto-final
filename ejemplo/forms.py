from django import forms
from ejemplo.models import Familiar
from ejemplo.models import Automovil
from ejemplo.models import Mascota

class Buscar(forms.Form):
  nombre = forms.CharField(max_length=100,
                          widget=forms.TextInput(attrs={"placeholder": "Busque algo..."}))

class FamiliarForm(forms.ModelForm):
  class Meta:
    model = Familiar
    fields = ['nombre', 'direccion', 'numero_pasaporte','fecha_nacimiento']

#autmovil

class AutomovilForm(forms.ModelForm):
  class Meta:
    model = Automovil
    fields = ['marca', 'modelo', 'color','cantidad_de_puertas','fecha_patentamiento']

#mascota

class MascotaForm(forms.ModelForm):
  class Meta:
    model = Mascota
    fields = ['nombre', 'animal', 'edad','fecha_adopcion']