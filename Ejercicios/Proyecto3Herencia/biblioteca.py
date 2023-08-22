
class Biblioteca:
    """Clase que representa una biblioteca."""
    
    def __init__(self):
        self.materiales = []

    def agregar_material(self, material):
        self.materiales.append(material)

    def mostrar_materiales(self):
        print("Materiales en la biblioteca:")
        for material in self.materiales:
            material.mostrar()
            print("-------------------------------")
