# gui.py
import tkinter as tk
from tkinter import ttk, messagebox
from data_manager import DataManager
from graph_manager import GraphManager
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import pandas as pd
from pandastable import Table

class AppGUI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Gestión de Asignaturas y Resultados")


        self.data_manager = DataManager()
        self.graph_manager = GraphManager(self.data_manager)

        self.setup_ui()

    def setup_ui(self):
        # Pestañas principales
        tab_control = ttk.Notebook(self.root)
        tab_agregar_asignatura = ttk.Frame(tab_control)
        tab_registrar_resultados = ttk.Frame(tab_control)
        tab_visualizar_grafo = ttk.Frame(tab_control) 
        tab_ver_datos = ttk.Frame(tab_control)

        tab_control.add(tab_agregar_asignatura, text='Agregar Asignatura')
        tab_control.add(tab_registrar_resultados, text='Registrar Resultados')
        tab_control.add(tab_visualizar_grafo, text='Visualizar Grafo') 
        tab_control.add(tab_ver_datos, text='Ver Datos')

        tab_control.pack(expand=1, fill="both")

        self.setup_tab_agregar_asignatura(tab_agregar_asignatura)
        self.setup_tab_registrar_resultados(tab_registrar_resultados)
        self.setup_tab_visualizar_grafo(tab_visualizar_grafo)
        self.setup_tab_ver_datos(tab_ver_datos)

    def setup_tab_agregar_asignatura(self, tab):
        ttk.Label(tab, text="Nombre de la Asignatura:").grid(column=0, row=0, padx=10, pady=10, sticky=tk.W)
        self.asignatura_nombre = ttk.Entry(tab, width=30)
        self.asignatura_nombre.grid(column=1, row=0, padx=10, pady=10, sticky=tk.W)

        ttk.Label(tab, text="Grado/Año:").grid(column=0, row=1, padx=10, pady=10, sticky=tk.W)
        self.asignatura_grado = ttk.Entry(tab, width=30)
        self.asignatura_grado.grid(column=1, row=1, padx=10, pady=10, sticky=tk.W)

        ttk.Button(tab, text="Agregar Asignatura", command=self.agregar_asignatura).grid(column=0, row=2, columnspan=2, padx=10, pady=10, sticky=tk.W+tk.E)

    def setup_tab_registrar_resultados(self, tab):
        ttk.Label(tab, text="Seleccionar Asignatura:").grid(column=0, row=0, padx=10, pady=10, sticky=tk.W)
        self.asignatura_seleccionada = ttk.Combobox(tab, width=27, state="readonly")
        self.asignatura_seleccionada.grid(column=1, row=0, padx=10, pady=10, sticky=tk.W)
        self.asignatura_seleccionada['values'] = list(self.data_manager.asignaturas.keys())

        ttk.Label(tab, text="Nombre del Estudiante:").grid(column=0, row=1, padx=10, pady=10, sticky=tk.W)
        self.estudiante_nombre = ttk.Entry(tab, width=30)
        self.estudiante_nombre.grid(column=1, row=1, padx=10, pady=10, sticky=tk.W)

        self.estudiante_aprobado = tk.IntVar()
        ttk.Checkbutton(tab, text="Aprobado", variable=self.estudiante_aprobado).grid(column=0, row=2, columnspan=2, padx=10, pady=10, sticky=tk.W)

        ttk.Button(tab, text="Registrar Resultado", command=self.registrar_resultado).grid(column=0, row=3, columnspan=2, padx=10, pady=10, sticky=tk.W+tk.E)

    def setup_tab_visualizar_grafo(self, tab):
        # Crear el contenedor para el grafo
        self.figure_frame = ttk.Frame(tab)
        self.figure_frame.pack(fill=tk.BOTH, expand=True)
        
        # Añadir un botón para actualizar el grafo
        self.update_graph_button = ttk.Button(tab, text="Actualizar Grafo", command=self.actualizar_grafo)
        self.update_graph_button.pack(pady=10)

    def setup_tab_ver_datos(self, tab):
        # Preparar los datos para el DataFrame
        data = {
            'Asignatura': [],
            'Estudiante': [],
            'Aprobado': [],
        }
        
        # Iterar sobre las asignaturas y sus resultados
        for asignatura, resultados in self.data_manager.resultados.items():
            if resultados:  # Si hay resultados para la asignatura
                for estudiante, aprobado in resultados:
                    data['Asignatura'].append(asignatura)
                    data['Estudiante'].append(estudiante)
                    data['Aprobado'].append('Sí' if aprobado else 'No')
            else:
                # Agregar la asignatura incluso si no hay resultados para mantener la consistencia
                data['Asignatura'].append(asignatura)
                data['Estudiante'].append('---')
                data['Aprobado'].append('---')
        
        # Crear el DataFrame de pandas
        dataframe = pd.DataFrame(data)

        # Crea el Frame de PandasTable dentro de la pestaña
        frame = ttk.Frame(tab)
        frame.pack(fill=tk.BOTH, expand=True)
        
        # Mostrar el DataFrame en la GUI
        table = Table(frame, dataframe=dataframe, showtoolbar=True, showstatusbar=True)
        table.show()



    def actualizar_grafo(self):
        # Elimina cualquier visualización de grafo existente en el contenedor
        for widget in self.figure_frame.winfo_children():
            widget.destroy()
        
        # Genera el grafo utilizando GraphManager
        self.graph_manager.visualizar_grafo(self.figure_frame)

    def agregar_asignatura(self):
        nombre = self.asignatura_nombre.get()
        grado = self.asignatura_grado.get()
        if nombre and grado:
            self.data_manager.agregar_asignatura(nombre, grado)
            messagebox.showinfo("Éxito", "Asignatura agregada correctamente")
            self.asignatura_seleccionada['values'] = list(self.data_manager.asignaturas.keys())  # Actualizar la lista de asignaturas

            # Limpiar los campos
            self.asignatura_nombre.delete(0, tk.END)
            self.asignatura_grado.delete(0, tk.END)
        else:
            messagebox.showwarning("Advertencia", "Todos los campos son obligatorios")

    def registrar_resultado(self):
        asignatura = self.asignatura_seleccionada.get()
        estudiante = self.estudiante_nombre.get()
        aprobado = bool(self.estudiante_aprobado.get())
        if asignatura and estudiante:
            self.data_manager.agregar_resultado(asignatura, estudiante, aprobado)
            messagebox.showinfo("Éxito", "Resultado registrado correctamente")
        
            # Limpiar los campos
            self.estudiante_nombre.delete(0, tk.END)
            self.estudiante_aprobado.set(0)  # Asumiendo que es un CheckBox y quieres deseleccionarlo
            self.asignatura_seleccionada.set('')  # Si quieres resetear el combobox, asumiendo que '' es un valor no válido

        else:
            messagebox.showwarning("Advertencia", "Todos los campos son obligatorios")

    def run(self):
        self.root.mainloop()



