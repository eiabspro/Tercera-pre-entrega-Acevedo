from django.shortcuts import render
from entidades.models import *

from entidades.forms import *

# Create your views here.
def home(request):
    return render(request, "entidades/index.html")

def autores(request):
    contexto = {"autores": Autor.objects.all()}
    return render(request, "entidades/autores.html", contexto)

def libros(request):
    contexto = {"libros": Libro.objects.all()}
    return render(request, "entidades/libros.html", contexto)

def usuarios(request):
    contexto = {"usuarios": Usuario.objects.all()}
    return render(request, "entidades/usuarios.html", contexto)

def prestamos(request):
    contexto = {"prestamos": Prestamo.objects.all()}
    return render(request, "entidades/prestamos.html", contexto)

def acerca(request):
    return render(request, "entidades/acerca.html")

def contacto(request):
    return render(request, "entidades/contacto.html")

def autorForm(request):
    if request.method == "POST":
        miForm = AutorForm(request.POST)
        if miForm.is_valid():
            autor_nombre = miForm.cleaned_data.get("nombre")
            autor_apellido = miForm.cleaned_data.get("apellido")
            autor_fecha_nacimiento = miForm.cleaned_data.get("fecha_nacimiento")
            autor_nacionalidad = miForm.cleaned_data.get("nacionalidad")
            autor = Autor(nombre=autor_nombre, apellido=autor_apellido, fecha_nacimiento=autor_fecha_nacimiento, nacionalidad=autor_nacionalidad)
            autor.save()
            contexto = {"autores": Autor.objects.all() }
            return render(request, "entidades/autores.html", contexto)
    else:
        miForm = AutorForm()

    return render(request, "entidades/autoresForm.html", {"form": miForm})

def libroForm(request):
    if request.method == "POST":
        miForm = LibroForm(request.POST)
        if miForm.is_valid():
            libro_titulo = miForm.cleaned_data.get("titulo")
            libro_fecha_publicacion = miForm.cleaned_data.get("fecha_publicacion")
            libro_genero = miForm.cleaned_data.get("genero")
            libro_isbn = miForm.cleaned_data.get("isbn")
            libro_autor = miForm.cleaned_data.get("autor")
            libro = Libro(titulo=libro_titulo, fecha_publicacion=libro_fecha_publicacion, genero=libro_genero, isbn=libro_isbn, autor=libro_autor)
            libro.save()
            contexto = {"libros": Libro.objects.all() }
            return render(request, "entidades/libros.html", contexto)
    else:
        miForm = LibroForm()

    return render(request, "entidades/librosForm.html", {"form": miForm})

def usuarioForm(request):
    if request.method == "POST":
        miForm = UsuarioForm(request.POST)
        if miForm.is_valid():
            usuario_nombre = miForm.cleaned_data.get("nombre")
            usuario_apellido = miForm.cleaned_data.get("apellido")
            usuario_email = miForm.cleaned_data.get("email")
            usuario_fecha_registro = miForm.cleaned_data.get("fecha_registro")
            usuario = Usuario(nombre=usuario_nombre, apellido=usuario_apellido, email=usuario_email, fecha_registro=usuario_fecha_registro)
            usuario.save()
            contexto = {"usuarios": Usuario.objects.all() }
            return render(request, "entidades/usuarios.html", contexto)
    else:
        miForm = UsuarioForm()

    return render(request, "entidades/usuariosForm.html", {"form": miForm})

def prestamoForm(request):
    if request.method == "POST":
        miForm = PrestamoForm(request.POST)
        if miForm.is_valid():
            prestamo_libro = miForm.cleaned_data.get("libro")
            prestamo_usuario = miForm.cleaned_data.get("usuario")
            prestamo_fecha_prestamo = miForm.cleaned_data.get("fecha_prestamo")
            prestamo_fecha_devolucion = miForm.cleaned_data.get("fecha_devolucion")
            prestamo = Prestamo(libro=prestamo_libro, usuario= prestamo_usuario, fecha_prestamo=prestamo_fecha_prestamo, fecha_devolucion=prestamo_fecha_devolucion)
            prestamo.save()
            contexto = {"prestamos": Prestamo.objects.all() }
            return render(request, "entidades/prestamos.html", contexto)
    else:
        miForm = PrestamoForm()

    return render(request, "entidades/prestamosForm.html", {"form": miForm})

# Buscar y encontrar
def buscarLibro(request):
    return render(request, "entidades/buscarLibro.html")

def encontrarLibro(request):
    if request.GET["buscar"]:
        patron = request.GET["buscar"]
        cursos = Libro.objects.filter(titulo__icontains=patron)
        contexto = {'libros': cursos}
    else:
        contexto = {'libros': Libro.objects.all()}
    return render(request, "entidades/libros.html", contexto)
