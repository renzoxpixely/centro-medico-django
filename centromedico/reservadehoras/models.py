from django.db import models
from datetime import datetime
# Create your models here.







class Category(models.Model):
    sucursal = models.CharField(max_length=30, unique=True)
    codigo = models.CharField(max_length=30, unique=True)

    class Meta:
        verbose_name = "sucursal"
        verbose_name_plural = "sucursales"
    def __str__(self):
       return '%s %s' % (self.sucursal, self.codigo)

class Product(models.Model):
    rclient = models.CharField(max_length=200, verbose_name="Rut del cliente")
    nclient = models.CharField(max_length=200, verbose_name="Nombre del cliente")
    fnac = models.DateTimeField(auto_now=True,verbose_name="Fecha de nacimiento")
    correo = models.EmailField(max_length=200, verbose_name="Correo electronico")
    phone = models.IntegerField( verbose_name="Numero de telefono")
    
    category = models.ForeignKey(
        Category,
        related_name='products',
        on_delete=models.PROTECT,
        default=1
    )
    date = models.DateTimeField(default=datetime.now, blank=True,verbose_name="Fecha")

    class Meta:
        verbose_name = "reserva"
        verbose_name_plural = "reservas"
      
    def __str__(self):
       return '%s %s' % (self.rclient, self.nclient)
        
