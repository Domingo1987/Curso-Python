
from material_bibliografico import MaterialBibliografico, Mostrable

class Libro(MaterialBibliografico, Mostrable):
    """Clase que representa un libro en la biblioteca."""
    
    def __init__(self, titulo, autor, anio_publicacion, genero, ISBN):
        super().__init__(titulo, autor, anio_publicacion)
        self.genero = genero
        self.ISBN = ISBN

    def mostrar(self):
        print("Libro:")
        print(f"Título: {self.titulo}")
        print(f"Autor: {self.autor.nombre}")
        print(f"Año de Publicación: {self.anio_publicacion}")
        print(f"Género: {self.genero}")
        print(f"ISBN: {self.ISBN}")

    def mostrar_detalle(self):
        print("Detalles del libro:")
        print(f"Título: {self.titulo}")
        print(f"ISBN: {self.ISBN}")
