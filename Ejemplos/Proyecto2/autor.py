
class Autor:
    """Clase que representa a un autor de material bibliográfico."""
    
    def __init__(self, nombre, nacionalidad, fecha_nacimiento):
        self.nombre = nombre
        self.nacionalidad = nacionalidad
        self.fecha_nacimiento = fecha_nacimiento

    def mostrar(self):
        print("Autor:")
        print(f"Nombre: {self.nombre}")
        print(f"Nacionalidad: {self.nacionalidad}")
        print(f"Fecha de Nacimiento: {self.fecha_nacimiento}")
