from django.http import HttpResponse
from django.shortcuts import render
from .models import Curso

# Create your views here.

def curso(request, nombre, camada):

    mi_curso = Curso(nombre=nombre, camada=camada)
    mi_curso.save()

    return HttpResponse(f'Se generó el curso de {mi_curso.nombre} en la camada {mi_curso.camada}')