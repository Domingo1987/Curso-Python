# Definimos la clase base Autor
class Autor:
    def __init__(self, nombre):
        self.nombre = nombre

    def informacion(self):
        return f"Nombre: {self.nombre}"

# Creamos una subclase Escritor que hereda de Autor
class Escritor(Autor):
    def __init__(self, nombre, genero):
        super().__init__(nombre)
        self.genero = genero

    def informacion(self):
        return f"{super().informacion()} - Género Literario: {self.genero}"

# Definimos una segunda clase base
class Academico(Autor):
    def __init__(self, nombre, universidad):
        super().__init__(nombre)
        self.universidad = universidad

    def informacion(self):
        return f"{super().informacion()} - Universidad: {self.universidad}"


def imprimir_informacion_autor(autor):
    print("Nombre:", autor.nombre)
    if isinstance(autor, Escritor):
        print("Género Literario:", autor.genero)
    if isinstance(autor, Academico):
        print("Universidad:", autor.universidad)

def main():
    miAutor = Autor("Roberto")
    print(miAutor.informacion())

    miEscritor = Escritor("Luis", "Fantasia")
    print(miEscritor.informacion())

    miAcademico= Academico("Lucia", "Jarbard")
    print(miAcademico.informacion())

if __name__ == "__main__":
    main()