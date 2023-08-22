from colorama import Fore, Back, Style

# Colores para Fore y Back 
Fores = [Fore.BLACK, Fore.RED, Fore.GREEN, Fore.YELLOW, Fore.BLUE, Fore.MAGENTA, Fore.CYAN, Fore.WHITE]
Backs = [Back.BLACK, Back.RED, Back.GREEN, Back.YELLOW, Back.BLUE, Back.MAGENTA, Back.CYAN, Back.WHITE]

# Estilos de colorama (Style)
Styles = [Style.RESET_ALL,Style.DIM, Style.NORMAL, Style.BRIGHT]

def contar_palabras(texto):
    return len(texto.split())

def verificar_ortografia(texto):
    return "Ortografía verificada."

def ajustar_margenes(texto, margen_izquierdo=10, margen_derecho=10):
    return ' ' * margen_izquierdo + texto + ' ' * margen_derecho

def pintar_palabra(texto, palabra_clave, fore=0, back=0, style=0, **kwargs):
    palabras_resaltadas = []
    for word in texto.split():
        if word == palabra_clave:
            palabras_resaltadas.append(f"{Fores[fore]}{Backs[back]}{Styles[style]}{word}{Styles[0]}")
        else:
            palabras_resaltadas.append(word)
    return ' '.join(palabras_resaltadas)

def pintar_palabra_rec(texto, palabra_clave, fore=0, back=0, style=0, inicio=0, **kwargs):
    posicion = texto.find(palabra_clave, inicio)
    if posicion == -1:
        return texto
    palabra_resaltada = f"{Fores[fore]}{Backs[back]}{Styles[style]}{palabra_clave}{Styles[0]}"
    texto = texto[:posicion] + palabra_resaltada + texto[posicion + len(palabra_clave):]
    return pintar_palabra_rec(texto, palabra_clave, fore, back, style, inicio=posicion + len(palabra_resaltada), **kwargs)

def pintar_palabra_rec2(texto, palabra_clave, fore=0, back=0, style=0, palabras=None, index=0):
    if palabras is None:
        palabras = texto.split()
    if index == len(palabras):
        return ' '.join(palabras)
    if palabras[index] == palabra_clave:
        palabras[index] = f"{Fores[fore]}{Backs[back]}{Styles[style]}{palabras[index]}{Styles[0]}"
    return pintar_palabra_rec2(texto, palabra_clave, fore, back, style, palabras, index + 1)

def invertir_palabras_rec(texto, palabras=None, index=None):
    if palabras is None and index is None:
        palabras = texto.split()
        index = len(palabras) - 1
    if index < 0:
        return ''
    return palabras[index] + ' ' + invertir_palabras_rec(texto, palabras, index - 1)
