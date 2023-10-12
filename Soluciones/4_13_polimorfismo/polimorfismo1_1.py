# Roberto 4 de octubre de 2023
# Definimos la clase base Musico
class Musico:
    def instrumento(self):
        return f"El músico toca un instrumento."

# Definimos la clase hija Guitarrista
class Guitarrista(Musico):
    def instrumento(self):
        return f"{super().instrumento()} Que es la guitarra"

# Definimos la clase hija Baterista
class Baterista(Musico):
    def instrumento(self):
        return f"{super().instrumento()} Que es la bateria"

# Creamos un objeto de la clase Guitarrista
guitarrista = Guitarrista()
# Creamos un objeto de la clase Baterista
baterista = Baterista()

# Llamamos a los métodos instrumento()
print(baterista.instrumento())
print(guitarrista.instrumento())