
def capitalize_first_letters(text):
    """Capitaliza la primera letra de cada palabra en una cadena.
    
    Utiliza la función capitalize() para capitalizar la primera letra de una palabra.
    Documentación oficial de capitalize(): https://docs.python.org/3/library/stdtypes.html#str.capitalize
    
    Utiliza la función split() para dividir la cadena en palabras.
    Documentación oficial de split(): https://docs.python.org/3/library/stdtypes.html#str.split
    """
    return ' '.join(word.capitalize() for word in text.split())

def reverse_text(text):
    """Invierte una cadena de texto."""
    return text[::-1]

def contar_vocales(text):
    """Cuenta las vocales en una cadena de texto."""
    return sum(1 for char in text.lower() if char in 'aeiouáéíóú')

def reemplazar_vocales(text, reemplazo="*"):
    """Reemplaza las vocales en una cadena por un caracter especificado (por defecto '*')."""
    return ''.join(reemplazo if char in 'aeiouáéíóú' else char for char in text.lower())

if __name__ == "__main__":
    # Pruebas para las funciones
    print(capitalize_first_letters("hola mundo"))  # Debe imprimir "Hola Mundo"
    print(reverse_text("hola"))  # Debe imprimir "aloh"
    print(contar_vocales("murciélago"))  # Debe imprimir 5
    print(reemplazar_vocales("murciélago", "-"))  # Debe imprimir "m-rc--l-g-"
