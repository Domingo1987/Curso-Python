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
    def __init__(self, intrumento):
        super().__init__(intrumento)

    def tocar(self):
        return f"{super().tocar()}"

class Baterista(Musico):
    def __init__(self, intrumento):
        super().__init__(intrumento)

    def tocar(self):
        return f"{super().tocar()}"

def main():
    miBanda = [Guitarrista("guitarra"),Guitarrista("bajo"), Guitarrista("charango"),Baterista("bateria")]
    for musicos in miBanda:
        print(musicos.tocar())
    

if __name__ == "__main__":
    main()