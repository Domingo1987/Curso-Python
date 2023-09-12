#DESAFIO 1
class Autor:
    # Constructor de la clase
    def __init__(self, nombre, nacionalidad):
        self.nombre = nombre
        self.nacionalidad = nacionalidad
        self.libros = []
   
    def agregar_libro(self, libro):
        self.libros.append(libro)
    def eliminar_libro(self, libro):
        self.libros.pop(libro)
        
    def mostrar_autor(self):
        print(f"Nombre: {self.nombre}")
        print(f"Nacionalidad: {self.nacionalidad}")
        print(f"libro: {self.libros}")

autor1 = Autor("Gabriel García Márquez", "Colombiano")
autor1.agregar_libro("100 anios de Soledad")
autor1.agregar_libro("El amor en tiempos de colera")
autor1.agregar_libro("El coronel no tiene quien lo escriba")
#autor1.eliminar libro("0")
print(autor1.nombre)
print(autor1.nacionalidad)
print(autor1.libros)