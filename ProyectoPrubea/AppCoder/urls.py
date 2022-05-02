from django.urls import path
from .views import curso, entregables, estudiantes, inicio, profesores

urlpatterns = [
    path('', inicio),
    path('agrega-curso/<nombre>/<camada>/', curso),
    path('profesores/', profesores),
    path('estudiantes/', estudiantes),
    path('entregables/', entregables),
]
