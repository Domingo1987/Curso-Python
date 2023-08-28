import threading
import time
import random
import tkinter as tk

# Clase base Filosofo
class Filosofo(threading.Thread):
    def __init__(self, id, tenedor_izq, tenedor_der, status_label=None, log_text=None):
        super().__init__()
        self.id = id
        self.tenedor_izq = tenedor_izq
        self.tenedor_der = tenedor_der
        self.comidas = 0
        self.fallos = 0
        self.detener = False
        self.status_label = status_label
        self.log_text = log_text

    def update_status(self, status, color):
        if self.status_label:
            self.status_label.config(text=f"Filósofo {self.id+1}: {status}", background=color)
        if self.log_text:
            self.log_text.insert(tk.END, f"Filósofo {self.id+1} está {status.lower()}.\n")
            self.log_text.see(tk.END)

    def generar_informe(self):
        informe = f"Filósofo {self.id+1} - Comidas: {self.comidas}, Fallos: {self.fallos}"
        return informe