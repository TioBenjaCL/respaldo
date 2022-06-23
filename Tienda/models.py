from django.db import models

# Create your models here.
class Cliente(models.Model):
    idCliente = models.AutoField(primary_key=True,verbose_name="ID Cliente")
    nombre = models.CharField(max_length=20,verbose_name="Nombre Cliente",blank=False,null=False)
    nombreUsuario = models.CharField(max_length=20,verbose_name="Nombre Usuario",blank=False,null=False)
    correo = models.CharField(max_length=20,verbose_name="Correo Cliente",blank=False,null=False)
    contraseña = models.CharField(max_length=8,verbose_name="contraseña1",blank=False,null=False)
    scontraseña = models.CharField(max_length=8,verbose_name="contraseña2",blank=False,null=False)

    def __str__(self):
        return self.nombre
    
class Producto(models.Model):
    idProducto = models.AutoField(primary_key=True,verbose_name="Id Producto")
    nombreProducto = models.CharField(max_length=20,verbose_name="Nombre Del Producto",blank=False,null=False)
    tipoProducto = models.CharField(max_length=20,verbose_name="Tipo de producto",blank=False,null=False)
    fotoProducto = models.ImageField(upload_to="producto",blank=False,null=False)
    precio = models.IntegerField(verbose_name="precio",blank=False,null=False)
    descripcion = models.CharField(max_length=30,verbose_name="Descripcion",blank=False,null=False)

    def __str__(self):
        return self.nombreProducto

