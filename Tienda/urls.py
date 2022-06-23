from django.contrib import admin
from django.urls import path
from .views import principal,carrito,confirmacion,envio,inicio_sesion,ofertas,pedido,productos,registro,usuario,inicio_sesion_Admin,Mod_Ofertas,Modificacion_Admin,Principal_Admin,registro_Admin,Resumen_A,Resumen_total,Traslado_Admin,registroC,productos1,logiado,añadirProducto,registroP

urlpatterns = [
    path('',principal,name="principal"),
    path('principal',principal,name="principal1"),
    path('carrito',carrito,name="carrito"),
    path('confirmacion',confirmacion,name="confirmacion"),
    path('envio',envio,name="envio"),
    path('inicio_sesion',inicio_sesion,name="inicio_sesion"),
    path('ofertas',ofertas,name="ofertas"),
    path('pedido',pedido,name="pedido"),
    path('productos',productos,name="productos"),
    path('registro',registro,name="registro"),
    path('usuario',usuario,name="usuario"),
    path('inicio_sesion_Admin',inicio_sesion_Admin,name="inicio_sesion_Admin"),
    path('Mod_Ofertas',Mod_Ofertas,name="Mod_Ofertas"),
    path('Modificacion',Modificacion_Admin,name="Modificacion"),
    path('Principal_Admin',Principal_Admin,name="Principal_Admin"),
    path('registro_Admin',registro_Admin,name="registro_Admin"),
    path('Resumen_A',Resumen_A,name="Resumen_A"),
    path('Resumen_total',Resumen_total,name="Resumen_total"),
    path('Traslado_Admin',Traslado_Admin,name="Traslado_Admin"),
    path('registroC',registroC,name="registroC"),
    path('logiado',logiado,name="logiado"),
    path('añadirProducto',añadirProducto,name="añadirProducto"),
    path('registroP',registroP,name="registroP"),
]
