
# Definición de la clase Libro
class Libro:
    # Constructor de la clase
    def __init__(self, titulo="", genero="", ISBN=""):
        self.titulo = titulo
        self.genero = genero
        self.ISBN = ISBN

    # Método para mostrar los detalles del libro
    def mostrar_libro(self):
        print(f"Título: {self.titulo}")
        print(f"Género: {self.genero}")
        print(f"ISBN: {self.ISBN}")
