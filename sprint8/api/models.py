from django.db import models

# Create your models here.
class Dato(models.Model):
    nombre=models.CharField(max_length=50)
    apellido=models.CharField(max_length=50)
    tipo_cuenta=models.CharField(max_length=50)
    saldo_cuenta=models.IntegerField()
    tipo_prestamo=models.CharField(max_length=50)
    total_prestamo=models.IntegerField()
    direccion=models.CharField(max_length=50)
    creacion=models.DateTimeField(auto_now=True)
    actualizacion=models.DateTimeField(auto_now=True)

class Meta:
    ordering=("-creacion")
    verbose_name="Cliente"
    verbose_name_plural="Clientes"

def __str__(self):
    return self.nombre