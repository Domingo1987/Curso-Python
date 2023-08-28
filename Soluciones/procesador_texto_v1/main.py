from procesador_texto import *
from rich.prompt import Prompt #https://rich.readthedocs.io/en/stable/prompt.html

#mi_texto = "Este libro que es un libro muy bonito, no es mi libro, pero es un muy buen libro"
#mi_texto = Prompt.ask("Ingrese un texto para procesar")
mi_texto = "El lenguaje de programación Python ha experimentado un auge significativo en las últimas décadas. Python, debido a su sintaxis clara y legible, se ha convertido en una herramienta esencial para científicos, ingenieros y desarrolladores. Es ampliamente reconocido que Python ha influido en múltiples áreas del conocimiento, desde la ciencia de datos hasta el desarrollo web. La comunidad de Python es especialmente activa, proporcionando constantes actualizaciones y bibliotecas que expanden aún más las capacidades del lenguaje. Además, Python cuenta con una plataforma de desarrollo colaborativo en la que profesionales de todo el mundo aportan con módulos y paquetes para facilitar tareas específicas. Los novatos en programación suelen encontrar en Python un excelente punto de partida. Esto se debe en gran parte a la vasta cantidad de recursos educativos disponibles, muchos de los cuales son ofrecidos por la misma comunidad de Python. Además, universidades de todo el mundo han adoptado Python como el lenguaje principal en sus currículos de ciencias de la computación. A medida que el mundo avanza hacia una era digital aún más integrada, la relevancia de Python no muestra signos de disminución. Estudios recientes sugieren que Python podría seguir siendo el lenguaje de programación dominante en la próxima década. En conclusión, Python ha demostrado ser no solo un lenguaje de programación versátil, sino también una herramienta esencial para la academia y la industria."


mi_texto = pintar_palabra_rec(mi_texto, 'Python', 3, 4, 3, 0)

print(mi_texto)




""" dsadasdasasdsa
print(f"La cantidad de palabras del texto es {contar_palabras(mi_texto)}")
mi_texto2 = pintar_palabra(mi_texto, 'biblioteca', fore=2, back=5, style=3)
print(f"\n{mi_texto}")
"""











# Ejemplo de uso
"""oracion = "Hola, este es un ejemplo"
resultado = invertir_palabras_rec(oracion).strip()  # .strip() para eliminar espacios adicionales al final
print(f"\n{resultado}")  # Debería imprimir: "ejemplo un es este Hola,"
"""