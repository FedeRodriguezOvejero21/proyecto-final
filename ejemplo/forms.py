from django import forms
from ejemplo.models import Familiar

class Buscar(forms.Form):
  nombre = forms.CharField(max_length=100)
  direccion = forms.CharField(max_length=200) 
  numero_pasaporte = forms.IntegerField() 
  fecha_nacimiento= models.DateField()

class FamiliarForm(forms.ModelForm):
  class Meta:
    model = Familiar
    fields = ['nombre', 'direccion', 'numero_pasaporte','fecha_nacimiento']