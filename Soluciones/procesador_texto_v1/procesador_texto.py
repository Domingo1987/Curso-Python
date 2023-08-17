# procesador_texto.py

from colorama import Fore, Back, Style

# Colores para Fore y Back 
# BLACK 0,RED 1,GREEN 2,YELLOW 3,BLUE 4,MAGENTA 5,CYAN 6,WHITE 7.
Fores = [Fore.BLACK, Fore.RED]
Backs = [Back.BLACK]

# Estilos de colorama (Style)
# RESET_ALL 0, DIM 1, NORMAL 2, BRIGHT 3.
Styles = [Style.RESET_ALL,Style.DIM, Style.NORMAL, Style.BRIGHT]

# Definición de la clase Procesador
class Procesador:
    # Constructor de la clase
    def __init__(self, texto=""):
        self.texto = texto

    def contar_palabras(texto):
        return len(texto.split())

    def verificar_ortografia(texto):
        # Simulamos una función que verifica la ortografía.
        # En una aplicación real, esto podría ser más complejo.
        return "Ortografía verificada."

    def ajustar_margenes(texto, margen_izquierdo=10, margen_derecho=10):
        return ' ' * margen_izquierdo + texto + ' ' * margen_derecho
    
    def pintar_palabra(self, palabra_clave, fore=0, back=0, style=0, **kwargs):
        for word in self.texto.split():
            if word == palabra_clave:
                print(f"{Fores[fore]}{Backs[back]}{Styles[style]}{word}{Styles[0]}",**kwargs)
            else:
                print(f"<{word}>")
           

        
