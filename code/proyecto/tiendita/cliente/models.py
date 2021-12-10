from django.db import models

# Create your models here.
class Cliente(models.Model):
    cedula = models.CharField(max_length=10, unique=True)
    nombre = models.CharField(max_length=50, null=False)
    apellido = models.CharField(max_length=50, null=False)
    fecha_nacimiento = models.DateField(blank=True, null=True)
    correo_electronico = models.EmailField()
