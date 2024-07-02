# Generated by Django 5.0.6 on 2024-06-30 19:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('entidades', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='autor',
            options={'ordering': ['apellido'], 'verbose_name': 'Autor', 'verbose_name_plural': 'Autores'},
        ),
        migrations.AlterModelOptions(
            name='libro',
            options={'ordering': ['titulo'], 'verbose_name': 'Libro', 'verbose_name_plural': 'Libros'},
        ),
        migrations.AlterModelOptions(
            name='prestamo',
            options={'ordering': ['fecha_prestamo'], 'verbose_name': 'Préstamo', 'verbose_name_plural': 'Préstamos'},
        ),
        migrations.AlterModelOptions(
            name='usuario',
            options={'ordering': ['nombre'], 'verbose_name': 'Usuario', 'verbose_name_plural': 'Usuarios'},
        ),
    ]
