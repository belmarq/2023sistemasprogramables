from django.db import models

# Create your models here.
class Sensor(models.Model):
    nombre = models.CharField(max_length=255)

class Actuador(models.Model):
    nombre = models.CharField(max_length=255)


class Lectura(models.Model):
    sensor = models.ForeignKey(Sensor, on_delete=models.PROTECT, null=False)
    valor = models.FloatField(default=0, null=False)
    fecha = models.DateTimeField(null=False)


class Escritura(models.Model):
    actuador = models.ForeignKey(Actuador, on_delete=models.PROTECT, null=False)
    valor = models.FloatField(default=0, null=False)
    fecha = models.DateTimeField(null=False)


class Cliente(models.Model):
    nombre = models.CharField(max_length=255)


class ClienteSensor(models.Model):
    sensor = models.ForeignKey(Sensor, on_delete=models.PROTECT, null=False)
    cliente = models.ForeignKey(Cliente, on_delete=models.PROTECT, null=False)


class ClienteActuador(models.Model):
    actuador = models.ForeignKey(Actuador, on_delete=models.PROTECT, null=False)
    cliente = models.ForeignKey(Cliente, on_delete=models.PROTECT, null=False)
