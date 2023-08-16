# Desafio 1

# Funcion que toma una lista y devuelve suma y promedio
def suma_prom_list(lista):
    # Sumo los elementos de la lista
    sumi = sum(lista)
    # Hallo el promedio de los elementos de la lista
    promi = sumi / len(lista)
    return sumi, promi

# Inicio de mi programa

miLista = [4,5,8,9,12,7,8,6,1,6] # Defino la lista que voy a utilizar
if len(miLista)!=0:
    suma, promedio = suma_prom_list(miLista) # Llamo a la funcion definida y cargo lo que devuelve en dos variables
    print(f"La suma de los valores de la lista es {suma} y el promedio de sus valores {promedio}")
else:
    print("La lista esta vacia")