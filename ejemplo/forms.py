from django import forms
from ejemplo.models import Familiar

class Buscar(forms.Form):
  nombre = forms.CharField(max_length=100,
                          widget=forms.TextInput(attrs={"palceholder": "Busque algo..."}))

class FamiliarForm(forms.ModelForm):
  class Meta:
    model = Familiar
    fields = ['nombre', 'direccion', 'numero_pasaporte','fecha_nacimiento']