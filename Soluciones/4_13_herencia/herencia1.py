# Definimos la clase base Autor
class Autor:
    def __init__(self, nombre):
        self.__nombre = nombre

    def setNombre(self, nombre):
        self.__nombre = nombre

    def getNombre(self):
        return self.__nombre

# Creamos una subclase Escritor que hereda de Autor
class Escritor(Autor):
    def __init__(self, nombre, genero):
        super().__init__(nombre)
        self.genero = genero

# Definimos una segunda clase base
class Academico:
    def __init__(self, universidad):
        self.universidad = universidad

# Instanciamos un objeto de la clase Escritor
"""escritor = Escritor("Gabriel García Márquez", "Realismo Mágico")
print(escritor.nombre, escritor.genero)
"""
# Creamos una clase que hereda de Escritor y Academico
class EscritorAcademico(Escritor, Academico):
    def __init__(self, nombre, genero, universidad):
        Escritor.__init__(self, nombre, genero)
        Academico.__init__(self, universidad)

""" 
Desafio 1: 
Crea una clase Novelista que herede de Escritor y añade un atributo para el número de novelas escritas. 
"""
class Novelista(Escritor):
    def __init__(self, nombre, genero, cant_novelas):
        super().__init__(nombre, genero)
        self.cant_novelas = cant_novelas

def main():
    novelista = Novelista("Gabriel García Márquez", "Realismo Mágico", "51")
    print(novelista.nombre, novelista.genero, novelista.cant_novelas)

if __name__ == "__main__":
    main()