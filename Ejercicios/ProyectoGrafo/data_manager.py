import json

class DataManager:
    def __init__(self):
        self.asignaturas = {}  # clave: nombre de asignatura, valor: grado
        self.resultados = {}  # clave: nombre de asignatura, valor: lista de tuplas (nombre de estudiante, aprobado)
        self.datos_archivo = "datos_asignaturas.json"  # Nombre del archivo para guardar los datos
        self.cargar_datos()  # Cargar datos existentes al inicializar

    def cargar_datos(self):
        try:
            with open(self.datos_archivo, 'r') as archivo:
                datos = json.load(archivo)
                self.asignaturas = datos['asignaturas']
                self.resultados = {k: [(tup[0], tup[1]) for tup in v] for k, v in datos['resultados'].items()}  # Asegurar que los valores se carguen correctamente como listas de tuplas
        except FileNotFoundError:
            print("No se encontró el archivo de datos. Se creará uno nuevo al guardar.")

    def guardar_datos(self):
        datos = {
            'asignaturas': self.asignaturas,
            'resultados': self.resultados,
        }
        with open(self.datos_archivo, 'w') as archivo:
            json.dump(datos, archivo, indent=4)

    def agregar_asignatura(self, nombre, grado):
        if nombre not in self.asignaturas:
            self.asignaturas[nombre] = grado
            self.resultados[nombre] = []
            self.guardar_datos()  # Guardar cambios

    def agregar_resultado(self, asignatura, estudiante, aprobado):
        if asignatura in self.resultados:
            self.resultados[asignatura].append((estudiante, aprobado))
            self.guardar_datos()  # Guardar cambios
