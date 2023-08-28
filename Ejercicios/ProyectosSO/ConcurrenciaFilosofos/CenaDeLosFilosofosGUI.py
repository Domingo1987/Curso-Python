import tkinter as tk
from tkinter import ttk
from Principal import Principal
from Log import Log
from ManejadorExcepciones import ManejadorExcepciones

class CenaDeLosFilosofosGUI:
    def __init__(self, master):
        self.master = master
        self.master.title('Cena de los Filósofos')
        self.master.geometry('600x600')
        self.principal = None

        self.log_text = tk.Text(self.master, wrap='word', height=15, width=50)
        self.log_text.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

        self.version_combobox = ttk.Combobox(self.master, values=["seguro", "inseguro", "inanicion"], state="readonly")
        self.version_combobox.grid(row=1, column=0, padx=10, pady=10)
        self.version_combobox.current(0)  # Set default value

        self.start_button = ttk.Button(self.master, text='Iniciar', command=self.iniciar_filosofos)
        self.start_button.grid(row=2, column=0, padx=10, pady=10)

        self.stop_button = ttk.Button(self.master, text='Detener', command=self.detener_filosofos)
        self.stop_button.grid(row=2, column=1, padx=10, pady=10)

        self.status_labels = []
        for i in range(5):
            label = ttk.Label(self.master, text=f'Filósofo {i+1}: Pensando')
            label.grid(row=i+3, column=0, columnspan=2, padx=10, pady=10)
            self.status_labels.append(label)

    def iniciar_filosofos(self):
        try:
            version_seleccionada = self.version_combobox.get()
            Log.write(f"Iniciando el programa en modo {version_seleccionada}.", self.log_text)
            self.principal = Principal(5, version=version_seleccionada)
            self.principal.iniciar_filosofos()
            for i, filosofo in enumerate(self.principal.filosofos):
                filosofo.status_label = self.status_labels[i]
        except Exception as e:
            ManejadorExcepciones.handle(e, self.log_text)

    def detener_filosofos(self):
        if self.principal:
            informe = "\nINFORME:\n"
            for filosofo in self.principal.filosofos:
                filosofo.detener = True
                informe += filosofo.generar_informe() + "\n"
            self.log_text.insert(tk.END, informe)
            self.log_text.see(tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    app = CenaDeLosFilosofosGUI(root)
    root.mainloop()
