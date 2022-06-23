from django.shortcuts import render,redirect
from .models import Cliente,Producto
# Create your views here.
def principal(request):
    return render(request,'usuario/principal.html')
def carrito(request):
    return render(request,'usuario/carrito.html')
def confirmacion(request):
    return render(request,'usuario/confirmacion.html')
def envio(request):
    return render(request,'usuario/envio.html')
def inicio_sesion(request):
    return render(request,'usuario/inicio sesion.html')
def ofertas(request):
    return render(request,'usuario/ofertas.html')
def pedido(request):
    return render(request,'usuario/pedido.html')
def productos(request):
    return render(request,'usuario/productos.html')
def registro(request):
    return render(request,'usuario/registro.html')
def usuario(request):
    return render(request,'usuario/usuario.html')
def inicio_sesion_Admin(request):
    return render(request,'admin/inicio sesion_Admin.html')
def Mod_Ofertas(request):
    return render(request,'admin/Mod_Ofertas.html')
def Modificacion_Admin(request):
    return render(request,'admin/Modificacion.html')
def Principal_Admin(request):
    return render(request,'admin/Principal_Admin.html')
def registro_Admin(request):
    return render(request,'admin/registro_Admin.html')
def registroC(request):
    nombreP = request.POST['nombre']
    nombreU = request.POST['nombreu']
    correo = request.POST['correo']
    contraseña1 = request.POST['clave1']
    contraseña2 = request.POST['clave2']

    Cliente.objects.create(nombre = nombreP,nombreUsuario = nombreU, correo = correo, contraseña = contraseña1, scontraseña = contraseña2)
    return redirect('confirmacion')

def Resumen_A(request):
    return render(request,'admin/Resumen_Admin.html')
def Resumen_total(request):
    return render(request,'admin/Resument_total_admin.html')
def Traslado_Admin(request):
    return render(request,'admin/Translado_Admin.html')
def productos1(request):
    contexto = {"nombreProducto":"secadora","tipoProducto":"Electrodomestico"}
    return render(request,'usuario/plantilla.html',contexto)
def logiado(request):
    return render(request,'usuario/logiado.html')
def añadirProducto(request):
    return render(request,'admin/añadirProducto.html')
def registroP(request):
    imagen = request.FILES['fotografia']
    nombre = request.POST['nombre']
    Caracteristicas = request.POST['Caracteristicas']
    precio = request.POST['precio']

    Producto.objects.create(fotoProducto = imagen,nombreProducto = nombre, descripcion = Caracteristicas, precio = precio)
    return redirect('Mod_Ofertas')