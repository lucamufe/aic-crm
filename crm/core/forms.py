#from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import CostoProyectos


# Crear form para insertar registros
class InsertarDatos(forms.ModelForm):
    fecha = forms.DateField(required=True, widget=forms.widgets.DateInput(attrs={"placeholder":"Fecha", "class":"form-control"}), label="")
    ubicacion = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Ubicación", "class":"form-control"}), label="")
    categoria = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Categoría", "class":"form-control"}), label="")
    producto = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Producto", "class":"form-control"}), label="")
    medida = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Medida", "class":"form-control"}), label="")
    cantidad = forms.DecimalField(required=True, widget=forms.widgets.NumberInput(attrs={"placeholder":"Cantidad", "class":"form-control"}), label="")
    precio = forms.DecimalField(required=True, widget=forms.widgets.NumberInput(attrs={"placeholder":"Precio", "class":"form-control"}), label="")
    gastos = forms.DecimalField(required=True, widget=forms.widgets.NumberInput(attrs={"placeholder":"Gastos", "class":"form-control"}), label="")
    #usuario = User.username

    class Meta:
        model = CostoProyectos
        exclude =("usuario",)