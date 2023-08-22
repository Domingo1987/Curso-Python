from biblioteca import Autor, Libro

def main():
    # Creación de objetos para pruebas
    libro1 = Libro("El Principito", "Infantil", "12345")
    autor1 = Autor("Antoine de Saint-Exupéry", "Francés")

    # Mostrar libro y autor
    print("Detalles del Libro 1:")
    libro1.mostrar_libro()
    print("\nDetalles del Autor 1:")
    autor1.mostrar_autor()

    # Solicitar al usuario otro libro y mostrarlo
    titulo = input("Ingrese el titulo del libro")
    genero = input("Ingrese el genero del libro")
    ISBN = input("Ingrese el ISBN del libro")
    libro2 = Libro(titulo, genero, ISBN)
  
    nombre = input("Ingrese el nombre del autor")
    nacionalidad = input("Ingrese la nacionalidad del autor")
    autor2 = Autor(nombre, nacionalidad)
    
    libro2.mostrar_libro()
    autor2.mostrar_autor()


if __name__ == "__main__":
    main()
