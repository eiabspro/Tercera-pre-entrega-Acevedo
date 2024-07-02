from django import forms
from entidades.models import Autor, Libro, Usuario, Prestamo

class AutorForm(forms.Form):
    nombre = forms.CharField(max_length=50, required=True)
    apellido = forms.CharField(max_length=50, required=True)
    fecha_nacimiento = forms.DateField(
        required=True,
        widget=forms.DateInput(attrs={'type': 'date'})
    )
    nacionalidad = forms.CharField(max_length=50, required=True)

    def clean(self):
        cleaned_data = super().clean()
        nombre = cleaned_data.get('nombre')
        apellido = cleaned_data.get('apellido')

        if Autor.objects.filter(nombre=nombre, apellido=apellido).exists():
            raise forms.ValidationError('Ya existe un autor con este nombre y apellido.')

        return cleaned_data

class LibroForm(forms.Form):
    titulo = forms.CharField(max_length=50, required=True)
    fecha_publicacion = forms.DateField(
        required=True,
        widget=forms.DateInput(attrs={'type': 'date'})
    )
    genero = forms.CharField(max_length=50, required=True)
    isbn = forms.CharField(max_length=13, required=True)
    autor = forms.ModelChoiceField(queryset=Autor.objects.all(), required=True)

    def clean_isbn(self):
        isbn = self.cleaned_data.get('isbn')
        if not isbn.isdigit():
            raise forms.ValidationError('El ISBN debe contener solo números.')
        if len(isbn) not in [10, 13]:
            raise forms.ValidationError('El ISBN debe tener 10 o 13 dígitos.')
        if Libro.objects.filter(isbn=isbn).exists():
            raise forms.ValidationError('El ISBN ya existe.')
        return isbn

class UsuarioForm(forms.Form):
    nombre = forms.CharField(max_length=50, required=True)
    apellido = forms.CharField(max_length=50, required=True)
    email = forms.EmailField(max_length=50, required=True)
    fecha_registro = forms.DateField(
        required=True,
        widget=forms.DateInput(attrs={'type': 'date'})
    )

    def clean(self):
        cleaned_data = super().clean()
        nombre = cleaned_data.get('nombre')
        apellido = cleaned_data.get('apellido')

        if Usuario.objects.filter(nombre=nombre, apellido=apellido).exists():
            raise forms.ValidationError('Ya existe un usuario con este nombre y apellido.')

        return cleaned_data

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if Usuario.objects.filter(email=email).exists():
            raise forms.ValidationError('El correo electrónico ya existe.')
        return email

class PrestamoForm(forms.Form):
    libro = forms.ModelChoiceField(queryset=Libro.objects.all(), required=True)
    usuario = forms.ModelChoiceField(queryset=Usuario.objects.all(), required=True)
    fecha_prestamo = forms.DateField(
        required=True,
        widget=forms.DateInput(attrs={'type': 'date'})
    )
    fecha_devolucion = forms.DateField(
        required=True,
        widget=forms.DateInput(attrs={'type': 'date'})
    )
