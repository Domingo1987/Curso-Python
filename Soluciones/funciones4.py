def mcd(a, b):
    """
    Esta función implementa el algoritmo de Euclides para calcular el Máximo Común Divisor (MCD) 
    de dos números.
    """
    while b != 0:
        a, b = b, a % b
    return a

if __name__ == "__main__":
    # Prueba
    numero1 = 56
    numero2 = 98

    resultado = mcd(numero1, numero2)

    print(f"El MCD de {numero1} y {numero2} es: {resultado}")
