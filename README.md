# Tercera-pre-entrega-Acevedo

## Descripción

En esta entrega hay una aplicación web de una biblioteca virtual desarrollada con Django siguiendo el patrón MVT.
La aplicación permite el añadido y la vista de autores, libros, usuarios y prestamos. A su vez cuenta con una búsqueda de libros que interactua directamente con la db.

## Funcionalidades

**Autores**: Permite agregar y ver autores.
**Libros**: Permite agregar y ver libros.
**Usuarios**: Permite agregar y ver usuarios.
**Préstamos**: Permite agregar y ver los prestamos realizados.
---
**Acerca y Contacto**: Permite ver tanto información sobre la web y un contacto para consultas respectivamente

## Uso

1. Desde el panel de arriba se puede navegar por la vista de las distintas funcionalidad y dentro de cada una hay:

   a. Una opción para llenar un formulario correspondiente a la funcionalidad
   b. Un listado de los objetos agregados

2. desde "Inicio" puedes interactuar con el formulario de búsqueda de libros que interactúa con la db.

## Estructura del Proyecto:

entidades/: Contiene los modelos y formularios de la aplicación.
    entidades/templates/: Contiene las plantillas HTML para las vistas.
    entidades/static/: Contiene los archivos estáticos (CSS, JS, imágenes).
Proyecto/: Contiene la configuración principal de Django.
