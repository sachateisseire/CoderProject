from django.db import models

# Create your models here.

class Curso(models.Model):

    nombre = models.CharField('nombre', max_length=50)
    camada = models.IntegerField('camada')
    fecha_creacion = models.DateField('creacion', auto_now=False, auto_now_add=False, blank=True, null=True)

    def __str__(self) -> str:
        return f'{self.nombre}'

class Estudiante(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    email = models.EmailField()

    def __str__(self) -> str:
        return f'{self.nombre} {self.apellido}'

class Profesor(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    email = models.EmailField()
    profesion = models.CharField(max_length=30)

    def __str__(self) -> str:
        return f'{self.nombre} {self.apellido} | {self.profesion} '

class Entregable(models.Model):
    nombre = models.CharField(max_length=30)
    fechaDeEntrega = models.DateField()
    entregado = models.BooleanField()

    def __str__(self) -> str:
        return f'{self.nombre} | {self.fechaDeEntrega} | {self.entregado} '

    