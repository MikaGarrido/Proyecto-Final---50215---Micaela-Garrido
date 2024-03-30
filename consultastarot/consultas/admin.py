from django.contrib import admin

# Register your models here.
from .models import *

class ServicioAdmin(admin.ModelAdmin):
    list_display = ("nombre","descripcion")

admin.site.register(Cliente)
admin.site.register(Pregunta)
admin.site.register(ServicioTarot, ServicioAdmin)