from django import forms
from .models import ServicioTarot
from .models import Consulta, Cliente, Pregunta

import datetime
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm



class ServicioCreate(forms.Form):
    nombre = forms.CharField(max_length=400, required=True)
    descripcion = forms.CharField(max_length=400, required=True)

class PreguntaCreate(forms.Form):
    pregunta = forms.CharField(max_length=255, required=True)
    respuesta = forms.CharField(max_length=300, required=True)

class ClienteCreate(forms.Form):
    nombre = forms.CharField(max_length=100, required=True)
    email = forms.EmailField(required=True)
    fecha_nacimiento = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}), initial=datetime.date.today, required=True)

class ConsultaForm(forms.ModelForm):
    cliente = forms.ModelChoiceField(queryset=Cliente.objects.all(), required=True)
    servicio = forms.ModelChoiceField(queryset=ServicioTarot.objects.all(), required=True)
    pregunta = forms.ModelChoiceField(queryset=Pregunta.objects.all(), required=True)
    fecha_consulta = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}), initial=datetime.date.today, required=True)

    class Meta:
        model = Consulta
        fields = ['cliente', 'servicio', 'pregunta', 'fecha_consulta']
        
class RegistroForm(UserCreationForm): 
    email = forms.EmailField(required=True)   
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Confirma Contraseña", widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]

class UserEditForm(UserChangeForm): 
    email = forms.EmailField(required=True)   
    first_name = forms.CharField(label="Nombre/s", max_length=100, required=True)
    last_name = forms.CharField(label="Apellido/s", max_length=50, required=True)

    class Meta:
        model = User
        fields = ["email", "first_name", "last_name"]    

class AvatarForm(forms.Form):
    imagen = forms.ImageField(required=True)