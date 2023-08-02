import numpy as np

# Crear un tablero de juego 5x5
def crearTablero():
    tablero = np.zeros((5,5))
    return tablero

# Colocar tres barcos en posiciones aleatorias
#ndarray como argumento, nuestro tablero
def colocarBarcos(tablero):
    x, y = np.random.randint(0, 5, size=2)
    print(f"Los valores de x e y son {x},{y}")
    tablero[x,y]=1


# Función para verificar si hay un barco o agua en las coordenadas dadas

# Función para enmascarar el tablero

#Programa>> a JUGAR!
tabReal = crearTablero()
print("Tablero INICIAL\n")
print(tabReal)

colocarBarcos(tabReal)
print("Tablero con BARCOS\n")
print(tabReal)