from django.urls import path
from .views import curso, entregables, estudiantes, inicio, profesores

urlpatterns = [
    path('', inicio, name='Inicio'),
    path('agrega-curso/<nombre>/<camada>/', curso),
    path('profesores/', profesores, name='Profesores'),
    path('estudiantes/', estudiantes, name='Estudiantes'),
    path('entregables/', entregables, name='Entregables'),
]
