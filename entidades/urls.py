from django.urls import path, include
from entidades.views import *

urlpatterns = [
    path('', home, name="inicio"),
    path('autores/', autores, name="autores"),
    path('libros/', libros, name="libros"),
    path('usuarios/', usuarios, name="usuarios"),
    path('prestamos/', prestamos, name="prestamos"),
    
    path('acerca/', acerca, name="acerca"),
    path('contacto/', contacto, name="contacto"),

    # Formularios
    
    path('autoresForm/', autorForm, name="autoresForm"),
    path('librosForm/', libroForm, name="librosForm"),
    path('usuariosForm/', usuarioForm, name="usuariosForm"),
    path('prestamosForm/', prestamoForm, name="prestamosForm"),

    # Buscar
    path('buscarLibro/', buscarLibro, name="buscarLibro"),
    path('encontrarLibro/', encontrarLibro, name="encontrarLibro"),


]
