'''
Este código implementa un árbol binario para evaluar expresiones matemáticas. 
Los nodos del árbol contienen operadores como "+", "-", "*" y "/" o valores numéricos. 
Los nodos con operadores tienen dos hijos (izquierdo y derecho), y los nodos con valores 
numéricos son hojas del árbol, lo que significa que no tienen hijos.
'''
from graphviz import Digraph

def visualizar_arbol(raiz, nombre):
    dot = Digraph(comment='Árbol de Expresión')
    resultado = evaluar_expresion(raiz)
    texto_superior = "El resultado de la operacion es " + str(resultado) + "\n\n" 
   
   # Agregar texto en la parte superior
    with dot.subgraph() as s:
        s.attr(rank='source')
        s.node('top_text', texto_superior, shape='plaintext')
    
    def agregar_nodos(raiz, dot):
        if raiz is not None:
            if ((raiz.val == '+') | (raiz.val == '*') | (raiz.val == '/') | (raiz.val == '-')):
                dot.node(str(raiz), str(raiz.val), shape='ellipse', color='red')
            else:
                dot.node(str(raiz), str(raiz.val), shape='box', color='green')
            if raiz.izq is not None:
                dot.edge(str(raiz), str(raiz.izq))
                agregar_nodos(raiz.izq, dot)
            if raiz.der is not None:
                dot.edge(str(raiz), str(raiz.der))
                agregar_nodos(raiz.der, dot)
                
    agregar_nodos(raiz, dot)

   
    
    # Esta línea guardará la imagen en el mismo directorio con el nombre 'arbol_expresion.png'
    dot.render(nombre, format='png', cleanup=True)
    dot.view(nombre + '.png')

class Nodo:
    def __init__(self, key):
        self.izq = None
        self.der = None
        self.val = key

def print_preorder(raiz):
    if raiz:
        print(raiz.val, end=" ")
        print_preorder(raiz.izq)
        print_preorder(raiz.der)
        

def print_inorder(raiz):
    if raiz:
        print_inorder(raiz.izq)
        print(raiz.val, end=" ")
        print_inorder(raiz.der)
        

def print_postorder(raiz):
    if raiz:
        print_postorder(raiz.izq)
        print_postorder(raiz.der)
        print(raiz.val, end=" ")
        
def evaluar_expresion(raiz):
    if raiz:
        left = evaluar_expresion(raiz.izq)
        right = evaluar_expresion(raiz.der)
        
        if raiz.val == '+':
            return left + right
        elif raiz.val == '-':
            return left - right
        elif raiz.val == '*':
            return left * right
        elif raiz.val == '/':
            return left / right
        else:
            return int(raiz.val)
    else:
        return 0

def main():
    # Aqui comienza mi main

    # Expresion 5 + 3 * 4
    exp = Nodo ('+')
    exp.izq = Nodo (5)
    exp.der = Nodo ('*')
    exp.der.izq = Nodo (3)
    exp.der.der = Nodo (4)

    #print("Preorden\t")
    #print_preorder(exp)  # Salida esperada: 
    
    #print("\nPostorden\t")
    #print_postorder(exp)  # Salida esperada: 
    
    # Visualizar el árbol
    visualizar_arbol(exp, "arbol_expresion")

    # Obtener y mostrar la expresión y el resultado
    expresion = print_inorder(exp)
    resultado = evaluar_expresion(exp)
    print(f"\nExpresión: {expresion} = {resultado}")

    # Aqui finaliza mi main

if __name__ == "__main__":
    main()