
from material_bibliografico import MaterialBibliografico, Mostrable

class Revista(MaterialBibliografico, Mostrable):
    """Clase que representa una revista en la biblioteca."""
    
    def __init__(self, titulo, autor, anio_publicacion, numero_edicion, ISSN):
        super().__init__(titulo, autor, anio_publicacion)
        self.numero_edicion = numero_edicion
        self.ISSN = ISSN

    def mostrar(self):
        print("Revista:")
        print(f"Título: {self.titulo}")
        print(f"Autor: {self.autor.nombre}")
        print(f"Año de Publicación: {self.anio_publicacion}")
        print(f"Número de Edición: {self.numero_edicion}")
        print(f"ISSN: {self.ISSN}")

    def mostrar_detalle(self):
        print("Detalles de la revista:")
        print(f"Título: {self.titulo}")
        print(f"ISSN: {self.ISSN}")
