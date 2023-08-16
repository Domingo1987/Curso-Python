from procesador_texto import Procesador

mi_texto = "Cuando yo tenía seis años vi en un libro sobre la selva virgen que se titulaba 'Historias vividas', una magnífica lámina. Representaba una serpiente boa que se tragaba a una fiera. En el libro se afirmaba: 'La serpiente boa se traga su presa entera, sin masticarla. Luego ya no puede moverse y duerme durante los seis meses que dura su digestión'."
mi_texto2 = Procesador("En un pequeño pueblo al pie de las montañas, había una vieja biblioteca que todos en la comunidad adoraban. Aunque había edificios más modernos y tiendas con tecnología de punta alrededor, la biblioteca conservaba un encanto especial. Los niños acudían allí después de la escuela para sumergirse en mundos de fantasía y aventura. Los adultos, por su parte, encontraban en sus estanterías libros que les recordaban su juventud y otros que les ofrecían nuevos conocimientos. La bibliotecaria, doña Clara, conocía cada rincón de aquel lugar y cada libro que se encontraba en él. Siempre estaba dispuesta a recomendar una lectura o a ayudar a encontrar un libro perdido. Pero había un libro en particular que era su favorito. Era un libro antiguo, de tapas desgastadas y páginas amarillentas, pero con una historia cautivadora. Ella solía decir que ese libro tenía el poder de cambiar vidas. Y, en cierto modo, tenía razón. Cada persona que leía ese libro salía de la biblioteca con una sonrisa en el rostro y una nueva perspectiva de la vida.")

type(mi_texto2.texto)

largo = Procesador.contar_palabras(mi_texto2.texto)
print(f"La cantidad de palabras del texto es {largo}")
