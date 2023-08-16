import numpy as np
import random
import time
from tabulate import tabulate  # Necesitarás instalar este módulo con pip install tabulate

TAM = 5

# Crear un tablero de juego 5x5
def crearTablero():
    tablero = np.zeros((TAM,TAM))
    return tablero

# Colocar N barcos en posiciones aleatorias sin solapamiento
def colocarBarcos(tablero, n):
    for _ in range(n): 
        while True:
            x, y = np.random.randint(0, TAM, size=2)
            if tablero[x,y] == 0: # Si la celda está vacía
                tablero[x,y] = 1
                break # Salir del bucle una vez que se ha colocado el barco
    return tablero

# Crear un tablero enmascarado
def crearMascara(tablero, caracter):
    mascara = np.full(tablero.shape, caracter)
    return mascara

# IA para jugar contra
def turnoIA(tablero, mascara):
    while True:
        x, y = np.random.randint(0, TAM, size=2)
        if mascara[x,y] == 'X': # La IA solo dispara a las celdas que no ha disparado antes
            return x, y

# Función para verificar si hay un barco o agua en las coordenadas dadas
def verificarPosicion(x, y, tablero, mascara):
    if mascara[x, y] in ['A', 'B']: # Si la celda ya ha sido descubierta
        print(f"Ya disparaste a la posición ({x},{y}) antes.")
        return mascara, 0
    if tablero[x, y] == 1:
        print(f"¡Golpeaste un barco en la posición ({x},{y})!")
        mascara[x, y] = 'B'
        return mascara, 1
    else:
        print(f"Disparo al agua en la posición ({x},{y}).")
        mascara[x, y] = 'A'
        return mascara, 0

# Programa>> a JUGAR!
nombre = input("Ingrese su nombre: ")
num_barcos = int(input("Ingrese el número de barcos que desea colocar (máximo 8): "))
num_barcos = min(num_barcos, 8) # Asegurarse de que el número de barcos no sea mayor que 8

tabReal = crearTablero()
tabReal = colocarBarcos(tabReal, num_barcos)

mascara = crearMascara(tabReal, 'X')

print("Tablero INICIAL\n")
print(mascara)

start_time = time.time()

barcos_hundidos_jugador = 0
barcos_hundidos_IA = 0

for _ in range(num_barcos + 2): # Jugamos num_barcos + 2 turnos
    # Turno del jugador
    while True:
        x = int(input("Ingrese la coordenada x del disparo: "))
        y = int(input("Ingrese la coordenada y del disparo: "))
        if 0 <= x < 5 and 0 <= y < 5: # Verificar si las coordenadas están dentro del tablero
            break
        else:
            print("Por favor, ingrese coordenadas válidas (0-4).")

    mascara, hit = verificarPosicion(x, y, tabReal, mascara)
    barcos_hundidos_jugador += hit
    print(mascara)

    # Turno de la IA
    x, y = turnoIA(tabReal, mascara)
    print(f"La IA dispara a la posición ({x},{y})")
    mascara, hit = verificarPosicion(x, y, tabReal, mascara)
    barcos_hundidos_IA += hit
    print(mascara)

end_time = time.time()
tiempo = end_time - start_time

# Mostrar las estadísticas del juego al final
print("\nEstadísticas del juego:")
print(tabulate([
    ["Jugador", nombre, barcos_hundidos_jugador, tiempo],
    ["IA", "CeRPGPT", barcos_hundidos_IA, "-"]
], headers=["Tipo", "Nombre", "Barcos hundidos", "Tiempo transcurrido"], tablefmt='pretty'))