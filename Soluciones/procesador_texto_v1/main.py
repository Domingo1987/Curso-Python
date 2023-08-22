from procesador_texto import *

mi_texto = "Cuando yo tenía seis años vi en un libro sobre la selva virgen que se titulaba 'Historias vividas', una magnífica lámina. Representaba una serpiente boa que se tragaba a una fiera. En el libro se afirmaba: 'La serpiente boa se traga su presa entera, sin masticarla."
mi_texto2 = "En un pequeño pueblo al pie de las montañas, había una vieja biblioteca que todos en la comunidad adoraban. Aunque había edificios más modernos y tiendas con tecnología de punta alrededor, la biblioteca conservaba un encanto especial. Los niños acudían allí después de la escuela para sumergirse en mundos de fantasía y aventura. Los adultos, por su parte, encontraban en sus estanterías libros que les recordaban su juventud y otros que les ofrecían nuevos conocimientos. La bibliotecaria, doña Clara, conocía cada rincón de aquel lugar y cada libro que se encontraba en él. Siempre estaba dispuesta a recomendar una lectura o a ayudar a encontrar un libro perdido. Pero había un libro en particular que era su favorito. Era un libro antiguo, de tapas desgastadas y páginas amarillentas, pero con una historia cautivadora. Ella solía decir que ese libro tenía el poder de cambiar vidas. Y, en cierto modo, tenía razón. Cada persona que leía ese libro salía de la biblioteca con una sonrisa en el rostro y una nueva perspectiva de la vida. libro."

print(f"La cantidad de palabras del texto es {contar_palabras(mi_texto)}")

mi_texto2 = pintar_palabra_rec2(mi_texto2, 'libro', fore=2, back=5, style=3)
print(f"\n{mi_texto2}")

# Ejemplo de uso
oracion = "Hola, este es un ejemplo"
resultado = invertir_palabras_rec(oracion).strip()  # .strip() para eliminar espacios adicionales al final
print(f"\n{resultado}")  # Debería imprimir: "ejemplo un es este Hola,"
