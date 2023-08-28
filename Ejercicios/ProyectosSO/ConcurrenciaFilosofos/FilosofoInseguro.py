from Filosofo import Filosofo
import time
import random

# FilosofoInseguro hereda de Filosofo
class FilosofoInseguro(Filosofo):
    def __init__(self, id, tenedor_izq, tenedor_der, portero, status_label=None, log_text=None):
        super().__init__(id, tenedor_izq, tenedor_der, status_label, log_text)
        #self.portero = portero

    def run(self):
        while not self.detener:
            if self.tenedor_izq.levantar():
                if self.tenedor_der.levantar():
                    self.update_status("Comiendo", "green")
                    self.comidas += 1
                    time.sleep(random.uniform(0.5, 1.0))
                    self.tenedor_der.dejar()
                else:
                    self.fallos += 1
                    self.update_status("Esperando tenedores", "orange")
                    time.sleep(0.3)
                self.tenedor_izq.dejar()
            self.update_status("Pensando", "yellow")
            time.sleep(random.uniform(1, 3))