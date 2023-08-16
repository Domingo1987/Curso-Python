def tienen_elemento_comun(lista1, lista2):
    """
    Esta función toma dos listas como argumentos y devuelve True si tienen al menos 
    un elemento en común, de lo contrario devuelve False.
    """
    for elemento in lista1:            
        if elemento in lista2:
            return True
    return False

if __name__ == "__main__":
    # Prueba
    lista1 = [1, 2, 3, 4]
    lista2 = [5, 6, 7, 8]
    lista3 = [5, 6, 7, 4]

    resultado1 = tienen_elemento_comun(lista1, lista2)
    resultado2 = tienen_elemento_comun(lista1, lista3)

    print(f"Lista 1 y Lista 2 tienen un elemento en común: {resultado1}")
    print(f"Lista 1 y Lista 3 tienen un elemento en común: {resultado2}")
