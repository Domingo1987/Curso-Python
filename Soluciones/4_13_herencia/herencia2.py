from herencia1 import Autor, Escritor, EscritorAcademico, Academico

"""
Desafío 2: 
Implementa una clase Poeta que herede de Autor y tenga un atributo para el tipo de poesía que escribe.
"""
class Poeta(Autor):
    def __init__(self, nombre, tipo_poesia):
        super().__init__(nombre)
        self.tipo_poesia = tipo_poesia

def main():
    elPoeta = Poeta("Lucia","Dramatica")
    print(elPoeta.nombre, elPoeta.tipo_poesia)


if __name__ == "__main__":
    main()