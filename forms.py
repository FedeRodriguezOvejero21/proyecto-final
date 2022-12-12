from django import forms
from ejemplo.models import Familiar



class FamiliarForm(forms.ModelForm):
  class Meta:
    model = Familiar
    fields = ['nombre', 'direccion', 'numero_pasaporte','fecha_nacimiento']