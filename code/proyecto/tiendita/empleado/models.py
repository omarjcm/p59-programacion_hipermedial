from django.contrib.auth.models import User
from django.db import models
from django.db.models.fields import CharField

# Create your models here.
class Empleado(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    url = models.URLField(max_length=300, blank=True)
    biografia = models.TextField(blank=True)
    numero_telefono = CharField(max_length=20, blank=True)
    imagen = models.ImageField(
        upload_to='empleado/imagenes',
        blank=True,
        null=True
    )
    creado = models.DateTimeField(auto_now_add=True)
    modificado = models.DateTimeField(auto_now=True)