
from abc import ABC, abstractmethod

class MaterialBibliografico(ABC):
    """Clase abstracta que representa un material bibliográfico genérico."""
    
    def __init__(self, titulo, autor, anio_publicacion):
        self.titulo = titulo
        self.autor = autor
        self.anio_publicacion = anio_publicacion

    @abstractmethod
    def mostrar(self):
        pass

class Mostrable(ABC):
    """Interfaz que define un método para mostrar detalles adicionales."""
    
    @abstractmethod
    def mostrar_detalle(self):
        pass
