from django.db import models
from django.conf import settings

# Create your models here.
class Embarcacion(models.Model):
    nombre = models.CharField(max_length=120)
    eslora = models.DecimalField(max_digits=10, decimal_places=2)
    calado = models.DecimalField(max_digits=10, decimal_places=2)
    tipo = models.CharField(max_length=30)
    carga = models.IntegerField()
    costo = models.DecimalField(max_digits=10, decimal_places=2)
    fecha = models.DateField(auto_now=False, auto_now_add=True)
    company = models.CharField(max_length=100)
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL)
