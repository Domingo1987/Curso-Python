
from autor import Autor
from libro import Libro
from revista import Revista
from biblioteca import Biblioteca

def main():
    # Creación de un autor
    autor1 = Autor("Antoine de Saint-Exupéry", "Francés", "29/06/1900")
    
    # Creación de un libro y una revista usando el autor previamente creado
    libro1 = Libro("El Principito", autor1, 1943, "Infantil", "12345")
    revista1 = Revista("Ciencia Hoy", autor1, 2020, 150, "45678")
    
    # Creación de la biblioteca y agregado de los materiales
    biblioteca = Biblioteca()
    biblioteca.agregar_material(libro1)
    biblioteca.agregar_material(revista1)
    
    # Mostrar los materiales de la biblioteca
    biblioteca.mostrar_materiales()
    
    # Mostrar detalles adicionales
    print("Detalles adicionales:")
    libro1.mostrar_detalle()
    revista1.mostrar_detalle()

if __name__ == "__main__":
    main()
