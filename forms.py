from django import forms
class Buscar(forms.Form):
    nombre = forms.CharField(max_length=100)
    direccion = forms.CharField(max_length=200)
    numero_pasaporte = forms.IntegerField()
    fecha_nacimiento= forms.DateField(input_format=["%d/%m/%Y"])