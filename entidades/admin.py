from django.contrib import admin

# Register your models here.
from entidades.models import *

class AutorAdmin(admin.ModelAdmin):
    list_display = ("apellido", "nombre", "fecha_nacimiento", "nacionalidad")

class LibroAdmin(admin.ModelAdmin):
    list_display = ("titulo", "fecha_publicacion", "isbn", "autor", "genero")
    
class UsuarioAdmin(admin.ModelAdmin):
    list_display = ("apellido", "nombre", "email", "fecha_registro")

class PrestamoAdmin(admin.ModelAdmin):
    list_display = ("libro", "usuario", "fecha_prestamo", "fecha_devolucion")


admin.site.register(Autor, AutorAdmin)
admin.site.register(Libro, LibroAdmin)
admin.site.register(Usuario, UsuarioAdmin)
admin.site.register(Prestamo, PrestamoAdmin)