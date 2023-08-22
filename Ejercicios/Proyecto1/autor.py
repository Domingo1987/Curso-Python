class Autor:
    # Constructor de la clase
    def __init__(self, nombre="", nacionalidad=""):
        # Atributos privados
        self.nombre = nombre
        self.nacionalidad = nacionalidad


    # Método para mostrar los detalles del autor
    def mostrar_autor(self):
        print(f"Nombre: {self.nombre}")
        print(f"Nacionalidad: {self.nacionalidad}")

