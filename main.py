from pelicula import Pelicula
from catalogo_peliculas import CatalogoPeliculas as catalogo_peliculas

print('*** App Catalogo de Peliculas ***')
opcion = None
while opcion != 4:
    try:
        print('''Opciones:
        1. Agregar Pelicula
        2. Listar Peliculas
        3. Eliminar catalogo peliculas
        4. Salir''')
        opcion = int(input('Escribe tu opcion (1-4): '))
        if opcion == 1:  # Agregar pelicula
            nombre_pelicula = input('Dame el nombre de la pelicula: ')
            pelicula = Pelicula(nombre_pelicula)
            catalogo_peliculas.agregar_pelicula(pelicula)
        elif opcion == 2:  # Listar peliculas
            catalogo_peliculas.listar_peliculas()
        elif opcion == 3:  # Eliminar el catalogo de peliculas
            catalogo_peliculas.eliminar_peliculas()
    except Exception as e:
        print(f'Ocurrio un error: {e}')
        opcion = None
else:
    print('Salimos del programa...')
