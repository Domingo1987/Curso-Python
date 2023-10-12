"""
Crea una clase Musico que tenga un método instrumento y 
crea dos subclases Guitarrista y Baterista que sobrescriban el método instrumento. 
Instancia objetos de estas clases y demuestra el polimorfismo.
"""

class Musico:
    def __init__(self, intrumento):
        self.intrumento = intrumento

    def tocar(self):
        return f"Estoy tocando musica {self.intrumento}."

class Guitarrista(Musico):
    def __init__(self, intrumento, numCuerdas):
        super().__init__(intrumento)
        self.numCuerdas = numCuerdas

    def tocar(self):
        return f"{super().tocar()}"

class Baterista(Musico):
    def __init__(self, intrumento):
        super().__init__(intrumento)

    def tocar(self):
        return f"{super().tocar()}"

def main():
    # Aqui comienza mi main
    miBanda = [Guitarrista("guitarra",6),Guitarrista("bajo",4), Guitarrista("charango",8),Baterista("bateria")]
    for musicos in miBanda:
        print(musicos.tocar())
    # Aqui finaliza mi main

if __name__ == "__main__":
    main()