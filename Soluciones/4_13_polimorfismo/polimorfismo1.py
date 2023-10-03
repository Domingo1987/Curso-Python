# Definimos la clase base Autor
class Autor:
    def __init__(self, nombre):
        self.nombre = nombre

# Creamos una subclase Escritor que hereda de Autor
class Escritor(Autor):
    def __init__(self, nombre, genero):
        super().__init__(nombre)
        self.genero = genero

# Definimos una segunda clase base
class Academico(Autor):
    def __init__(self, nombre, universidad):
        super().__init__(nombre)
        self.universidad = universidad


def imprimir_informacion_autor(autor):
    print("Nombre:", autor.nombre)
    if isinstance(autor, Escritor):
        print("Género Literario:", autor.genero)
    if isinstance(autor, Academico):
        print("Universidad:", autor.universidad)

def main():
    miAutor = Academico("Roberto", "UTEC")
    imprimir_informacion_autor(miAutor)

if __name__ == "__main__":
    main()