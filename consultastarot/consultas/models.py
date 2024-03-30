from django.db import models
from django.utils import timezone
import datetime
from django.contrib.auth.models import User

# Create your models here.

class ServicioTarot(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=300)
    
    def __str__(self):
        return f'{self.nombre}'
    class Meta:
        verbose_name = "Servicio Tarot"
        verbose_name_plural = "Servicios Tarot"
    class Meta:
        ordering = ["nombre"]

class Pregunta(models.Model):
    pregunta = models.CharField(max_length=255)
    respuesta = models.CharField(max_length=300)
    servicio = models.ForeignKey(ServicioTarot, on_delete=models.CASCADE)  

    def __str__(self):
        return f'{self.pregunta}'

    
class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.EmailField()
    fecha_nacimiento = models.DateField(default=datetime.date.today)

    def __str__(self):
        return self.nombre

class Consulta(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    servicio = models.ForeignKey(ServicioTarot, on_delete=models.CASCADE)
    fecha_consulta = models.DateTimeField(default=timezone.now)
    pregunta = models.ForeignKey(Pregunta, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.cliente.nombre} - {self.servicio.nombre} - {self.fecha_consulta}"
    

class Avatar(models.Model):
    imagen = models.ImageField(upload_to="avatares")   
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user} {self.imagen}"