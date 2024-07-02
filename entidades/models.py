from django.db import models

# Create your models here.

class Autor(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    fecha_nacimiento = models.DateField()
    nacionalidad = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

    class Meta:
        unique_together = ('nombre', 'apellido')
        ordering = ['apellido', 'nombre']
        verbose_name = 'Autor'
        verbose_name_plural = 'Autores'

class Libro(models.Model):
    titulo = models.CharField(max_length=100)
    fecha_publicacion = models.DateField()
    genero = models.CharField(max_length=50)
    isbn = models.CharField(max_length=13, unique=True)
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE)

    def __str__(self):
        return self.titulo

    class Meta:
        ordering = ['titulo']
        verbose_name = 'Libro'
        verbose_name_plural = 'Libros'

class Usuario(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    email = models.EmailField(max_length=50, unique=True)
    fecha_registro = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

    class Meta:
        unique_together = ('nombre', 'apellido')
        ordering = ['apellido','nombre']
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'

class Prestamo(models.Model):
    libro = models.ForeignKey(Libro, on_delete=models.CASCADE)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    fecha_prestamo = models.DateField()
    fecha_devolucion = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"{self.libro.titulo} prestado a {self.usuario.nombre}"

    class Meta:
        ordering = ['fecha_prestamo']
        verbose_name = 'Préstamo'
        verbose_name_plural = 'Préstamos'
