from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from .models import *
from .models import Cliente
from .forms import *
from django.shortcuts import get_object_or_404



from django.contrib.auth import login, authenticate
from django.contrib.auth. forms import AuthenticationForm
from django.contrib.auth.views import PasswordChangeView

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required


# Hecho por Micaela Garrido <3.

def home(request):
    return render(request, "aplicacion/index.html")

#-----------------------Servicios
@login_required
def serviciotarot(request):
    servicios = ServicioTarot.objects.all().order_by("id")
    return render(request, 'aplicacion/serviciotarot.html', {'servicios': servicios})

@login_required
def servicioCreate(request):
    if request.method == "POST":
        miForm = ServicioCreate(request.POST)
        if miForm.is_valid():
            servicio_nombre = miForm.cleaned_data.get("nombre")
            servicio_descripcion = miForm.cleaned_data.get("descripcion")
            serviciotarot = ServicioTarot(nombre=servicio_nombre, descripcion=servicio_descripcion)
            serviciotarot.save()
            return render(request, 'aplicacion/index.html')
    else:
        miForm = ServicioCreate()

    return render(request, "aplicacion/servicioForm.html", {"form":miForm} )

@login_required
def servicioUpdate(request, id_serviciotarot):
    serviciotarot = ServicioTarot.objects.get(id=id_serviciotarot)
    if request.method == "POST":
        miForm = ServicioCreate(request.POST)
        if miForm.is_valid():
            serviciotarot.nombre = miForm.cleaned_data.get("nombre")
            serviciotarot.descripcion = miForm.cleaned_data.get("descripcion")
            serviciotarot.save()

            return redirect(reverse_lazy('serviciotarot'))
    else:
        miForm = ServicioCreate(initial={'nombre':serviciotarot.nombre, 'descripcion':serviciotarot.descripcion})

    return render(request, "aplicacion/servicioForm.html", {"form":miForm} )

@login_required
def servicioDelete(request, id_serviciotarot):
    serviciotarot = ServicioTarot.objects.get(id=id_serviciotarot)
    serviciotarot.delete()
    return redirect(reverse_lazy('serviciotarot'))

#-------------------------Preguntas
@login_required
def pregunta(request):
    preguntas = Pregunta.objects.all().order_by("id")
    return render(request, 'aplicacion/pregunta.html', {'pregunta': preguntas})

@login_required
def preguntaCreate(request):
    if request.method == "POST":
        miForm = PreguntaCreate(request.POST)
        if miForm.is_valid():
            preg_pregunta = miForm.cleaned_data.get("pregunta")
            preg_respuesta = miForm.cleaned_data.get("respuesta")
            pregunta = Pregunta(pregunta=preg_pregunta, respuesta=preg_respuesta)
            pregunta.save()
            return render(request, 'aplicacion/index.html')
    else:
        miForm = PreguntaCreate()

    return render(request, "aplicacion/preguntaForm.html", {"form":miForm} )

@login_required
def preguntaUpdate(request, id_pregunta):
    pregunta = Pregunta.objects.get(id=id_pregunta)
    if request.method == "POST":
        miForm = PreguntaCreate(request.POST)
        if miForm.is_valid():
            pregunta.pregunta = miForm.cleaned_data.get("nombre")
            pregunta.respuesta = miForm.cleaned_data.get("descripcion")
            pregunta.save()

            return redirect(reverse_lazy('pregunta'))
    else:
        miForm = PreguntaCreate(initial={'pregunta':pregunta.pregunta, 'respuesta':pregunta.respuesta})

    return render(request, "aplicacion/preguntaForm.html", {"form":miForm} )

@login_required
def preguntaDelete(request, id_pregunta):
    pregunta = Pregunta.objects.get(id=id_pregunta)
    pregunta.delete()
    return redirect(reverse_lazy('pregunta'))

#------------------------ Clientes

@login_required
def cliente(request):
    clientes = Cliente.objects.all().order_by("id")
    return render(request, 'aplicacion/cliente.html', {'cliente': clientes})

@login_required
def clienteCreate(request):
    if request.method == "POST":
        miForm = ClienteCreate(request.POST)
        if miForm.is_valid():
            cliente_nombre = miForm.cleaned_data.get("nombre")
            cliente_email = miForm.cleaned_data.get("email")
            cliente_fechan = miForm.cleaned_data.get("fecha_nacimiento")
            cliente = Cliente(nombre=cliente_nombre, email=cliente_email, fecha_nacimiento=cliente_fechan)
            cliente.save()
            return render(request, 'aplicacion/index.html')
    else:
        miForm = ClienteCreate()

    return render(request, "aplicacion/clienteForm.html", {"form":miForm} )

@login_required
def clienteUpdate(request, id_cliente):
    cliente = Cliente.objects.get(id=id_cliente)
    if request.method == "POST":
        miForm = ClienteCreate(request.POST)
        if miForm.is_valid():
            cliente.nombre = miForm.cleaned_data.get("nombre")
            cliente.email = miForm.cleaned_data.get("email")
            cliente.fecha_nacimiento = miForm.cleaned_data.get("fecha_nacimiento")
            cliente.save()

            return redirect(reverse_lazy('cliente'))
    else:
        miForm = ClienteCreate(initial={'nombre':cliente.nombre, 'email':cliente.email, 'fecha_nacimiento':cliente.fecha_nacimiento})

    return render(request, "aplicacion/clienteForm.html", {"form":miForm} )

@login_required
def clienteDelete(request, id_cliente):
    cliente = Cliente.objects.get(id=id_cliente)
    cliente.delete()
    return redirect(reverse_lazy('cliente'))


#-----------------------------Consultas


def consulta(request):
    consultas = Consulta.objects.all().order_by("id")
    return render(request, 'aplicacion/consulta.html', {'consulta': consultas})


def consultaCreate(request):
    if request.method == "POST":
        miForm = ConsultaForm(request.POST)
        if miForm.is_valid():
            miForm.save()
            return render(request, 'aplicacion/consulta.html')
    else:
        miForm = ConsultaForm()

    return render(request, "aplicacion/consultaForm.html", {"form": miForm})

def consultaUpdate(request, id_consulta):
    consulta = Consulta.objects.get(id=id_consulta)
    if request.method == "POST":
        miForm = ConsultaForm(request.POST)
        if miForm.is_valid():
            consulta.cliente = miForm.cleaned_data.get("cliente")
            consulta.servicio = miForm.cleaned_data.get("servicio")
            consulta.fecha_consulta = miForm.cleaned_data.get("fecha_consulta")
            consulta.pregunta = miForm.cleaned_data.get("pregunta")
            consulta.save()

            return redirect(reverse_lazy('consulta'))
    else:
        miForm = ConsultaForm(initial={'consulta':consulta.cliente, 'servicio':consulta.servicio, 'fecha_consulta':consulta.fecha_consulta, 'pregunta':consulta.pregunta})

    return render(request, "aplicacion/consultaForm.html", {"form":miForm} )

def consultaDelete(request, id_consulta):
    consulta = Consulta.objects.get(id=id_consulta)
    consulta.delete()
    return redirect(reverse_lazy('consulta'))


#---------------------------------Buscar

@login_required
def buscarServicios(request):
    return render(request, "aplicacion/buscar.html")

@login_required
def encontrarServicios(request):
    patron = request.GET.get("buscar")
    if patron:
        servicios = ServicioTarot.objects.filter(nombre__icontains=patron)
    else:
        servicios = ServicioTarot.objects.all()

    contexto = {"servicios": servicios}
    return render(request, "aplicacion/serviciotarot.html", contexto)

#----------------Adicional

def acerca(request):
    return render(request, "aplicacion/acerca.html")

#----------------------Login, Logout, Authentication, Registration

def login_request(request):         
    if request.method == "POST":
        usuario = request.POST['username']
        clave = request.POST['password']
        user = authenticate(request, username=usuario, password=clave)
        if user is not None:
            login(request, user)
            #--------------------Avatar
            try:
                avatar = Avatar.objects.get(user=request.user.id).imagen.url
            except:
                avatar = "/media/avatares/default.png"
            finally:
                request.session["avatar"] = avatar

            #---------------------------

            return render(request, "aplicacion/index.html")
        else:
            return redirect(reverse_lazy('login'))
    else:
    # __ Si ingresa en el else es la primera vez 
        miForm = AuthenticationForm()

    return render(request, "aplicacion/login.html", {"form": miForm} )

def register(request):
    if request.method == "POST":
        miForm = RegistroForm(request.POST)

        if miForm.is_valid():
            usuario = miForm.cleaned_data.get("username")
            miForm.save()
            return redirect(reverse_lazy('home'))
    else:
    # __ Si ingresa en el else es la primera vez 
        miForm = RegistroForm()

    return render(request, "aplicacion/registro.html", {"form": miForm} )  

#------------------------Edición de Perfil, Cambio Clave, Avatar

@login_required
def editProfile(request):
    usuario = request.user
    if request.method == "POST":
        miForm = UserEditForm(request.POST)
        if miForm.is_valid():
            user = User.objects.get(username=usuario)
            user.email = miForm.cleaned_data.get("email")
            user.first_name = miForm.cleaned_data.get("first_name")
            user.last_name = miForm.cleaned_data.get("last_name")
            user.save()
            return redirect(reverse_lazy('home'))
    else:
    # __ Si ingresa en el else es la primera vez 
        miForm = UserEditForm(instance=usuario)

    return render(request, "aplicacion/editarPerfil.html", {"form": miForm} )    
   
class CambiarClave(LoginRequiredMixin, PasswordChangeView):
    template_name = "aplicacion/cambiar_clave.html"
    success_url = reverse_lazy("home")

@login_required
def agregarAvatar(request):
    if request.method == "POST":
        miForm = AvatarForm(request.POST, request.FILES)
        if miForm.is_valid():
            usuario = User.objects.get(username=request.user)
            #---- Borrar avatares viejos
            avatarViejo = Avatar.objects.filter(user=usuario)
            if len(avatarViejo) > 0:
                for i in range(len(avatarViejo)):
                    avatarViejo[i].delete()
            #---------------------------
            avatar = Avatar(user=usuario,
                            imagen=miForm.cleaned_data["imagen"])
            avatar.save()
            imagen = Avatar.objects.get(user=usuario).imagen.url
            request.session["avatar"] = imagen
            
            return redirect(reverse_lazy('home'))
    else:
    # __ Si ingresa en el else es la primera vez 
        miForm = AvatarForm()

    return render(request, "aplicacion/agregarAvatar.html", {"form": miForm} )      