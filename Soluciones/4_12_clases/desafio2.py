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

        for libro in self.libros:
            libro.mostrar_libro()
        


class Libro:
    # Constructor de la clase
    def __init__(self, titulo, genero, ISBN):
        self.titulo = titulo
        self.genero = genero
        self.ISBN = ISBN
        
    def mostrar_libro(self):
        print(f"Titulo: {self.titulo}")
        print(f"Genero: {self.genero} \t ISBN: {self.ISBN}")

autor1 = Autor("Gabriel García Márquez", "Colombiano")
libro1 = Libro("100 anios de Soledad","Drama","123")
autor1.agregar_libro(libro1)
libro2 = Libro("El amor en tiempos de colera","Suspenso","1234")
autor1.agregar_libro(libro2)

#autor1.agregar_libro("El amor en tiempos de colera")
#autor1.agregar_libro("El coronel no tiene quien lo escriba")
#autor1.eliminar libro("0")

autor1.mostrar_autor()