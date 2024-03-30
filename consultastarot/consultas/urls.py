from django.urls import path
from .views import *
from .forms import *
from django.contrib.auth.views import LogoutView

urlpatterns = [

    #Menu principal

    path('inicio/', home, name="home"),
    
    
    #Servicios

    path('serviciotarot/', serviciotarot, name="serviciotarot"),
    path('servicio_create/', servicioCreate, name="servicio_create"),
    path('servicio_update/<id_serviciotarot>/', servicioUpdate, name="servicio_update"),
    path('servicio_delete/<id_serviciotarot>/', servicioDelete, name="servicio_delete"),


    #Pregunta

    path('pregunta/',pregunta, name="pregunta"),
    path('pregunta_create/', preguntaCreate, name="pregunta_create"),
    path('pregunta_update/<int:id_pregunta>/', preguntaUpdate, name="pregunta_update"),
    path('pregunta_delete/<int:id_pregunta>/', preguntaDelete, name="pregunta_delete"),


    #Cliente

    path('cliente/', cliente, name="cliente"),
    path('cliente_create/', clienteCreate, name="cliente_create"),
    path('cliente_update/<int:id_cliente>/', clienteUpdate, name="cliente_update"),
    path('cliente_delete/<int:id_cliente>/', clienteDelete, name="cliente_delete"),


    #Consulta 

    path('consulta/', consulta, name="consulta"),
    path('consulta_create/<int:id_cliente>/', consultaCreate, name="consulta_create"),
    path('consulta_update/<int:pk>/', consultaUpdate, name="consulta_update"),
    path('consulta_delete/<int:pk>/', consultaDelete, name="consulta_delete"),



    #Buscar

    path('buscar_servicios/', buscarServicios, name="buscar_servicios"),
    path('encontrar_servicios/', encontrarServicios, name="encontrar_servicios"),

    #Acerca de mi

    path('acerca/', acerca, name="acerca_de_mi"),
    

    #Login, Logout, Registration

    path('login/', login_request, name="login"),
    path('logout/', LogoutView.as_view(template_name="aplicacion/logout.html") , name="logout"),
    path('registrar/', register, name="registrar"),
    
    #Edicion Perfil, Cambio de Clave, Avatar
    
    path('perfil/', editProfile, name="perfil"),
    path('<int:pk>/password/', CambiarClave.as_view(), name="cambiar_clave"),
    path('agregar_avatar/', agregarAvatar, name="agregar_avatar"),

]
