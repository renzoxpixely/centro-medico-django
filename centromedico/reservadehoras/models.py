from django.db import models
from datetime import datetime
# Create your models here.


from django import forms





class Project(models.Model):




    rclient = models.CharField(max_length=200, verbose_name="Rut del cliente")
    nclient = models.CharField(max_length=200, verbose_name="Nombre del cliente")
    fnac = models.DateTimeField(auto_now=True,verbose_name="Fecha de nacimiento")
    correo = models.EmailField(max_length=200, verbose_name="Correo electronico")
    phone = models.IntegerField( verbose_name="Numero de telefono")
    STATUS = (
          (1,  ('114 - San Nicolás')),
          (2, ('115 - San Pedro')),
          (3, ('115 - San Tomás')),
       )
       # [...]
    status = models.PositiveSmallIntegerField(
          choices=STATUS,
          default=1
          , verbose_name="Nombre de sucursal",
       )
    #nsucursal = models.CharField(max_length=200, verbose_name="Nombre de sucursal")
    created = models.DateTimeField(auto_now_add=True,verbose_name="Fecha de registro")
    updated = models.DateTimeField(auto_now=True,verbose_name="Fecha de edición")
    date = models.DateTimeField(default=datetime.now, blank=True,verbose_name="Fecha")





    class Meta:
        verbose_name = "reserva"
        verbose_name_plural = "reservas"
        ordering = ['-created']
    
    
    def __str__(self):
       return '%s %s' % (self.rclient, self.nclient)
        

      