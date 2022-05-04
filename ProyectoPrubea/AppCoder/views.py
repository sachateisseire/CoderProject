from django.http import HttpResponse
from django.shortcuts import render

from .forms import CursoFormulario, ProfesorFormulario
from .models import Curso, Profesor

# Create your views here.

def curso(request, nombre, camada):

    mi_curso = Curso(nombre=nombre, camada=camada)
    mi_curso.save()

    return render(request, 'AppCoder/cursos.html', {'nombre':nombre, 'camada':camada})

def profesores(request):

    return render(request, 'AppCoder/profesores.html')

def estudiantes(request):

    return render(request, 'AppCoder/estudiantes.html')

def entregables(request):

    return render(request, 'AppCoder/entregables.html')

def inicio(request):

    return render(request, 'AppCoder/inicio.html')

def cursoFormulario(request):

    if request.method == 'POST':

        print('**************************')
        print(request.POST)
    
        mi_formulario = CursoFormulario(request.POST)

        print('---------------------------')
        print(mi_formulario)

        if mi_formulario.is_valid:

            informacion = mi_formulario.cleaned_data

            nombre = informacion['nombre']
            camada = informacion['camada']
            fecha = informacion['fecha_creacion']

            mi_curso = Curso(nombre=nombre, camada=camada, fecha_creacion=fecha)
            mi_curso.save()

            return render(request, 'AppCoder/inicio.html')

    else:    

        mi_formulario = CursoFormulario()

    return render(request, 'AppCoder/cursoFormulario.html', {'miForm': mi_formulario})


def profesores(request):

    if request.method == 'POST':

        miFormulario = ProfesorFormulario(request.POST)

        print('----------', miFormulario)

        if miFormulario.is_valid():

            informacion = miFormulario.cleaned_data

            profesor = Profesor (nombre=informacion['nombre'], apellido=informacion['apellido'], email=informacion['email'], profesion=informacion['profesion'])

            profesor.save()

            return render(request, 'AppCoder/inicio.html')

    else:

        miFormulario= ProfesorFormulario()

    return render(request, 'AppCoder/profesores.html', {'miFormulario':miFormulario})




def leerProfesores(request):

    profesores = Profesor.objects.all()

    contexto = {"lista_profesores":profesores}

    return render(request, "AppCoder/leerProfesores.html", contexto)

def eliminarProfesor(request, id):

    profesor = Profesor.objects.get(id=id)
    profesor.delete()

    profesores = Profesor.objects.all()

    contexto = {"lista_profesores":profesores}

    return render(request, "AppCoder/leerProfesores.html", contexto)

