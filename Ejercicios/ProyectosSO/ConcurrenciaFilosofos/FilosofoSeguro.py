from Filosofo import Filosofo
import time
import random

# FilosofoSeguro hereda de Filosofo
class FilosofoSeguro(Filosofo):
    def __init__(self, id, tenedor_izq, tenedor_der, portero, status_label=None, log_text=None):
        super().__init__(id, tenedor_izq, tenedor_der, status_label, log_text)
        self.portero = portero
        self.bloqueos = 0  # Añadido específicamente para FilosofoSeguro

    def run(self):
        while not self.detener:
            if self.portero.entrar():
                if self.tenedor_izq.levantar():
                    if self.tenedor_der.levantar():
                        self.update_status("Comiendo", "green")
                        self.comidas += 1
                        time.sleep(random.uniform(1, 1.5))
                        self.tenedor_der.dejar()
                    else:
                        self.fallos += 1
                        self.update_status("Esperando tenedores", "red")
                        time.sleep(0.5)
                    self.tenedor_izq.dejar()
                self.portero.salir()
            else:
                self.bloqueos += 1
            self.update_status("Pensando", "yellow")
            time.sleep(random.uniform(1, 2))