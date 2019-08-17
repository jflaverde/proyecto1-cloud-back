from django.db import models
from django.contrib.auth.models import User
import datetime

# Create your models here.
class Empresa(models.Model):
    nombre = models.CharField(null=False, max_length=100)
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    url = models.CharField(null=False, max_length=100)

    def __str__(self):
        return self.nombre

class Proyecto(models.Model):
    nombre = models.CharField(null=False, max_length=100)
    descripcion = models.CharField(null=False, max_length=100)
    valor_estimado = models.FloatField(null=False)
    fecha_creacion= models.DateTimeField(default=datetime.datetime.now)

    def __str__(self):
        return self.nombre

class Estado(models.Model):
    nombre = models.CharField(null=False, max_length=100)

    def __str__(self):
        return self.nombre

class Diseño(models.Model):
    fecha_creacion = models.DateTimeField(default=datetime.datetime.now)
    estado = models.ForeignKey(Estado, on_delete=models.CASCADE, related_name='estado')
    ruta_diseño_original = models.CharField(null=False, max_length=100)
    ruta_diseño_procesado = models.CharField(null=False, max_length=100)
    formato = models.CharField(null=False, max_length=8)
    nombre_diseño_original = models.CharField(null=False, max_length=100)
    nombre_diseño_procesado = models.CharField(null=False, max_length=100)
    valor_estimado = models.FloatField(null=False)
    nombre_diseñador = models.CharField(null=False, max_length=100)
    apellido_diseñador = models.CharField(null=False, max_length=100)
    email_diseñador = models.CharField(null=False, max_length=100)

    def __str__(self):
        return self.nombre_diseño_original