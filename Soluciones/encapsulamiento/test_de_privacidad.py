from desafio1 import Autor, Libro

miAutor = Autor("Lucia","Uruguaya")
libro1Lucia = Libro("Pepe el sapo", "Comedia", "246")
miAutor.agregar_libro(libro1Lucia)

#miAutor.mostrar_autor()
miAutor.set_nacionalidad("Bielorrusa")

print(f"Puedo ver la nacionalidad de lucia: {miAutor.get_nacionalidad()}")
miAutor.mostrar_autor()
