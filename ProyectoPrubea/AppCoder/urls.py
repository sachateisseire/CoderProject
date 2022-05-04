from django.urls import path
from .views import curso, cursoFormulario, eliminarProfesor, entregables, estudiantes, inicio, leerProfesores, profesores

urlpatterns = [
    path('', inicio, name='Inicio'),
    path('agrega-curso/<nombre>/<camada>/', curso),
    path('profesores/', profesores, name='Profesores'),
    path('estudiantes/', estudiantes, name='Estudiantes'),
    path('entregables/', entregables, name='Entregables'),
    path('cursoFormulario/', cursoFormulario, name='cursoFormulario'),
    path('leerProfesores/', leerProfesores, name='LeerProfesores'),
    path('eliminarProfesor/<id>', eliminarProfesor, name='EliminarProfesor'),
]
