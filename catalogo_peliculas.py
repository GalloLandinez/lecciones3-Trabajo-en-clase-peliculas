import os

class CatalogoPeliculas:
    nombre_archivo = 'peliculas.txt'

    @classmethod
    def agregar_pelicula(cls, pelicula):
         with open(cls.nombre_archivo, 'a', encoding='utf8') as archivo:
             archivo.write(f'{pelicula.nombre}\n')

    @classmethod
    def listar_peliculas(cls):
        with open(cls.nombre_archivo, 'r', encoding='utf8') as archivo:
            print('*** Listado de Peliculas ***')
            print(archivo.read())

    @classmethod
    def eliminar_peliculas(cls):
        os.remove(cls.nombre_archivo)
        print(f'Archivo eliminado: {cls.nombre_archivo}')