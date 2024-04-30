# graph_manager.py
import tkinter
import networkx as nx
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class GraphManager:
    def __init__(self, data_manager):
        self.data_manager = data_manager
        self.G = nx.Graph()

    def construir_grafo(self):
        self.G.clear()  # Limpia el grafo para reconstruirlo
        for asignatura, grado in self.data_manager.asignaturas.items():
            # Añade los nodos con atributos adicionales si es necesario
            self.G.add_node(asignatura, grado=grado)

        # Para cada asignatura, verificar los estudiantes que la han aprobado
        for asignatura, resultados in self.data_manager.resultados.items():
            aprobados = [estudiante for estudiante, aprobado in resultados if aprobado]
            for otra_asignatura, otros_resultados in self.data_manager.resultados.items():
                if asignatura != otra_asignatura:
                    otros_aprobados = [estudiante for estudiante, aprobado in otros_resultados if aprobado]
                    # Si hay estudiantes que han aprobado ambas asignaturas, añadir una arista
                    if set(aprobados) & set(otros_aprobados):
                        self.G.add_edge(asignatura, otra_asignatura)

    def visualizar_grafo(self, frame):
        self.construir_grafo()  # Asegurarse de que el grafo esté actualizado

        fig = Figure(figsize=(8, 6))
        ax = fig.add_subplot(111)
        pos = nx.spring_layout(self.G)  # Puedes experimentar con diferentes disposiciones
        nx.draw(self.G, pos, ax=ax, with_labels=True, node_size=1500, node_color="skyblue", edge_color="gray", font_size=10, arrows=True)

        # Añade la figura a la interfaz de Tkinter
        canvas = FigureCanvasTkAgg(fig, master=frame)
        canvas.draw()
        canvas.get_tk_widget().pack(fill=tkinter.BOTH, expand=True)

