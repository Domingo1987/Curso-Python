class Libro:
    # Constructor de la clase
    def __init__(self, titulo="", genero="", ISBN=""):
        # Atributos privados
        self.__titulo = titulo
        self.__genero = genero
        self.__ISBN = ISBN

    # Métodos getter para los atributos
    def get_titulo(self):
        return self.__titulo

    def get_genero(self):
        return self.__genero

    def get_ISBN(self):
        return self.__ISBN

    # Métodos setter para los atributos
    def set_titulo(self, titulo):
        self.__titulo = titulo

    def set_genero(self, genero):
        self.__genero = genero

    def set_ISBN(self, ISBN):
        self.__ISBN = ISBN

    # Método para mostrar los detalles del libro
    def mostrar_libro(self):
        print(f"Título: {self.get_titulo()}")
        print(f"Género: {self.get_genero()}")
        print(f"ISBN: {self.get_ISBN()}")
