# Portero que permite deadlock


import threading
import time

class PorteroInseguro:
    def __init__(self, num_comensales):
        self.comensal = num_comensales - 1
        self.lock = threading.Lock()
        
    def entrar(self):
        with self.lock:
            if self.comensal > 0:
                self.comensal -= 1
                return True
            else:
                return False
            
            
    def salir(self):
        with self.lock:
            self.comensal += 1

    def obtener_intentos_entrada(self):  # Método para obtener el número de intentos de entrada
        return self.intentos_entrada


""""
class PorteroInseguro:
    def __init__(self, num_comensales):
        
        pass  # No necesita hacer nada en el constructor
        
    def entrar(self):
        return True  # Siempre permite entrar
            
    def salir(self):
        pass  # No necesita hacer nada al salir
"""