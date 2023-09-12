#DESAFIO 1
from typing import Any


class Autor:
    # Constructor de la clase
    def __init__(self, nombre, nacionalidad):
        self.__nombre = nombre
        self.__nacionalidad = nacionalidad
        self.__libros = []

    def get_nombre(self):
        return self.__nombre
    
    def set_nombre(self, nombre):
        self.__nombre = nombre
    
    def get_nacionalidad(self):
        return self.__nacionalidad
    
    def set_nacionalidad(self, nacionalidad):
        self.__nacionalidad = nacionalidad
   
    def agregar_libro(self, libro):
        self.__libros.append(libro)
    def eliminar_libro(self, libro):
        self.__libros.pop(libro)
        
    def mostrar_autor(self):
        print(f"Nombre: {self.__nombre}")
        print(f"Nacionalidad: {self.__nacionalidad}")

        for libro in self.__libros:
            libro.mostrar_libro()

class Libro:
    # Constructor de la clase
    def __init__(self, titulo, genero, ISBN):
        self.__titulo = titulo
        self.__genero = genero
        self.__ISBN = ISBN
        
    def mostrar_libro(self):
        print(f"Titulo: {self.__titulo}")
        print(f"Genero: {self.__genero} \t ISBN: {self.__ISBN}")
"""""
autor1 = Autor("Gabriel García Márquez", "Colombiano")
libro1 = Libro("100 anios de Soledad","Drama","123")
autor1.agregar_libro(libro1)
libro2 = Libro("El amor en tiempos de colera","Suspenso","1234")
autor1.agregar_libro(libro2)
libro2 = Libro("El coronel no tiene quien lo escriba","Drama","12345")
autor1.agregar_libro(libro2)

autor1.mostrar_autor()
"""""