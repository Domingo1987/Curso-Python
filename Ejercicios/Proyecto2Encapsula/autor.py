class Autor:
    # Constructor de la clase
    def __init__(self, nombre="", nacionalidad=""):
        # Atributos privados
        self.__nombre = nombre
        self.__nacionalidad = nacionalidad

    # Métodos getter para los atributos
    def get_nombre(self):
        return self.__nombre

    def get_nacionalidad(self):
        return self.__nacionalidad

    # Métodos setter para los atributos
    def set_nombre(self, nombre):
        self.__nombre = nombre

    def set_nacionalidad(self, nacionalidad):
        self.__nacionalidad = nacionalidad

    # Método para mostrar los detalles del autor
    def mostrar_autor(self):
        print(f"Nombre: {self.get_nombre()}")
        print(f"Nacionalidad: {self.get_nacionalidad()}")

