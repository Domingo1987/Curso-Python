from Filosofo import Filosofo
import time
import random

# FilosofoSeguro hereda de Filosofo
class FilosofoInanicion(Filosofo):
    def __init__(self, id, tenedor_izq, tenedor_der, portero, status_label=None, log_text=None):
        super().__init__(id, tenedor_izq, tenedor_der, status_label, log_text)
        self.portero = portero

    def run(self):
        while not self.detener:
            self.update_status("Pensando", "yellow")
            time.sleep(random.uniform(1, 2))
            
            while True:
                if self.tenedor_izq.levantar():  # Intenta tomar el tenedor izquierdo
                    if not self.tenedor_der.levantar():  # Verifica si el tenedor derecho está ocupado
                        self.tenedor_izq.dejar()  # Si está ocupado, deja el tenedor izquierdo
                        self.update_status("Esperando tenedores", "red")
                        self.fallos += 1
                        time.sleep(0.5)
                        continue  # Vuelve al inicio del ciclo while
                    else:
                        self.update_status("Comiendo", "green")
                        self.comidas += 1
                        time.sleep(random.uniform(1, 1.5))
                        self.tenedor_izq.dejar()  # Deja el tenedor izquierdo
                        self.tenedor_der.dejar()  # Deja el tenedor derecho
                        break  # Sale del ciclo while
                    