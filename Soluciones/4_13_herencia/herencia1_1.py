# Realizado por Roberto en 2023

class Escritor:
    def __init__(self, nombre):
        self.nombre = nombre

    def biografia(self):
        return f"El escritor {self.nombre} nació en el año 1900 en la ciudad de Madrid."

class Novelista(Escritor):
    def __init__(self, nombre, numero_novelas):
        super().__init__(nombre)
        self.numero_novelas = numero_novelas

    def biografia(self):
        return f"El novelista {self.nombre} nació en el año 1900 en la ciudad de Madrid. Ha escrito {self.numero_novelas} novelas."

def main():
    elNovelista = Novelista("Gabriel García Márquez", 10)
    print(elNovelista.biografia())
    elEscritor = Escritor("Gabriel García Márquez")
    print(elEscritor.biografia())  # Esto arrojará un AttributeError, ya que 'Escritor' object has no attribute 'nombre'


if __name__ == "__main__":
    main()
