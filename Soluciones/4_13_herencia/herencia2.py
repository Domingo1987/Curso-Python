from herencia1 import Autor

"""
Desafío 2: 
Implementa una clase Poeta que herede de Autor y tenga un atributo para el tipo de poesía que escribe.
"""
class Poeta(Autor):
    def __init__(self, nombre, tipo_poesia):
        super().__init__(nombre)
        #self.nombre = nombre
        self.__tipo_poesia = tipo_poesia
    
    def setTipoPoesia(self, tipo_poesia):
        self.__tipo_poesia = tipo_poesia

    def getTipoPoesia(self):
        return self.__tipo_poesia

def main():
    elAutor = Autor("Lucia")
    elPoeta = Poeta(elAutor.getNombre(),"Dramatica")
    print(elPoeta.getNombre(), elPoeta.getTipoPoesia())

if __name__ == "__main__":
    main()