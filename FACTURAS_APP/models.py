# Create your models here.
from django.db import models
from django.utils import timezone


class Liquidacion(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    publicada = models.BooleanField()


class Contrato(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    fecha = models.DateTimeField(default=timezone.now)
    liquidacion = models.ForeignKey(Liquidacion)


class Factura(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    fecha = models.DateTimeField(default=timezone.now)
    file = models.FileField(upload_to='documents/')
    contrato = models.ForeignKey(Contrato)
    liquidacion = models.ForeignKey(Liquidacion)
    precio = models.DecimalField(max_digits=6, decimal_places=2)
    iva = models.IntegerField()

    def _get_total(self):
        return self.precio * self.iva + self.precio
    total = property(_get_total)





