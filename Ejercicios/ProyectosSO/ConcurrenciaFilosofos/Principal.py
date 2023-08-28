from Tenedor import Tenedor
from PorteroSeguro import PorteroSeguro
from PorteroInseguro import PorteroInseguro
from FilosofoSeguro import FilosofoSeguro
from FilosofoInseguro import FilosofoInseguro
from FilosofoInanicion import FilosofoInanicion
import time

class Principal:
    def __init__(self, num_filosofos, version='seguro'):
        """
        Inicializa la simulación de la cena de los filósofos.

        :param num_filosofos: Número de filósofos en la cena.
        :param version: 'seguro' para la versión que evita el deadlock, 'inseguro' para la que lo permite.
        """
        self.num_filosofos = num_filosofos
        self.tenedores = [Tenedor(i) for i in range(num_filosofos)]
        
        # Escoge el tipo de portero y clase de filósofo según la versión
        if version == 'seguro':
            self.portero = PorteroSeguro(num_filosofos)
            FilosofoClass = FilosofoSeguro
        elif version == 'inseguro':
            self.portero = PorteroInseguro(num_filosofos)
            FilosofoClass = FilosofoInseguro
        else:
            self.portero = PorteroSeguro(num_filosofos)
            FilosofoClass = FilosofoInanicion
            
        # Inicializa los filósofos
        self.filosofos = [
            FilosofoClass(i, self.tenedores[i], self.tenedores[(i + 1) % num_filosofos], self.portero)
            for i in range(num_filosofos)
        ]

    def iniciar_filosofos(self):
        """
        Inicia la ejecución de los hilos de los filósofos y permite que comiencen a comer/pensar.
        """
        for filosofo in self.filosofos:
            filosofo.start()

        # Este sleep es solo para demostración. En un escenario real, podrías querer que esto se ejecute indefinidamente
        # o hasta que se cumpla una cierta condición.
        time.sleep(10)
