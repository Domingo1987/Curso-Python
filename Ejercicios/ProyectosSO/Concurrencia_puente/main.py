import pygame
import random
import threading
import time

# Inicializar pygame
pygame.init()

# Colores
BLANCO = (255, 255, 255)
GRIS = (200, 200, 200)

# Dimensiones de la pantalla
ANCHO = 1000
ALTO = 400
ESPACIO_AUTO = 90  # Espacio requerido por cada auto incluyendo margen
MAX_AUTOS = 3  # Máximo número de autos en espera

# Configuración de la pantalla y el reloj
pantalla = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Simulación del Puente")
reloj = pygame.time.Clock()

# Variables globales
coches_izquierda = []
coches_derecha = []
puente = []
preferencia = None  # Nueva variable para almacenar la preferencia del puente

# Cargar imágenes de los coches (coloca las imágenes en la misma carpeta que el script)
imagen_coche_blue = pygame.image.load("autitoRed.png")
imagen_coche_blue = pygame.transform.scale(imagen_coche_blue, (80, 40))
imagen_coche_blue.set_colorkey((255, 255, 255))

imagen_coche_red = pygame.image.load("autitoBlue.png")
imagen_coche_red = pygame.transform.scale(imagen_coche_red, (80, 40))
imagen_coche_red.set_colorkey((255, 255, 255))

# Clase Coche
class Coche:
    def __init__(self, direccion):
        self.direccion = direccion
        self.velocidad = 5
        self.offset_y = 0
        self.mover_arriba = True  # Añadimos esta línea para inicializar la variable
        
        if direccion == "I":
            self.x = len(coches_izquierda) * ESPACIO_AUTO
            self.y = ALTO // 2
            self.imagen = imagen_coche_red
        else:
            self.x = ANCHO - (len(coches_derecha) + 1) * ESPACIO_AUTO
            self.y = ALTO // 2
            self.imagen = imagen_coche_blue

    def mover(self):
        # Añadir efecto de "subir y bajar"
        if self.mover_arriba:
            self.offset_y -= 1
            if self.offset_y <= -5:
                self.mover_arriba = False
        else:
            self.offset_y += 1
            if self.offset_y >= 5:
                self.mover_arriba = True

        # Mover el coche
        if self.direccion == "I":
            self.x += self.velocidad
        else:
            self.x -= self.velocidad

    

    def dibujar(self, pantalla):
        if self in puente:
            if self.direccion == "I":
                pantalla.blit(self.imagen, (self.x, self.y + self.offset_y))
            else:
                pantalla.blit(self.imagen, (self.x, self.y + self.offset_y))
        else:
            if self.direccion == "I":
                indice = coches_izquierda.index(self)
                nueva_x = indice * ESPACIO_AUTO
            else:
                indice = coches_derecha.index(self)
                nueva_x = ANCHO - (indice + 1) * ESPACIO_AUTO
            pantalla.blit(self.imagen, (nueva_x, self.y + self.offset_y))


# Función para controlar el acceso al puente
def control_puente():
    global coches_izquierda, coches_derecha, puente, preferencia

    while True:
        if not puente:
            if coches_derecha and (preferencia == "D" or not coches_izquierda):
                puente.append(coches_derecha.pop(0))
                preferencia = "D"
            elif coches_izquierda and (preferencia == "I" or not coches_derecha):
                puente.append(coches_izquierda.pop(0))
                preferencia = "I"
        time.sleep(0.1)
# Configuración de la fuente para el texto
fuente = pygame.font.Font(None, 36)

# Función principal del juego
def main():
    global coches_izquierda, coches_derecha, puente, preferencia

    terminado = False

    # Iniciar el control del puente en un hilo separado
    threading.Thread(target=control_puente).start()

    while not terminado:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminado = True

        pantalla.fill(BLANCO)

        # Dibuja el puente
        pygame.draw.rect(pantalla, GRIS, [ANCHO//4, ALTO//2 - 10, ANCHO//2, 20])

        # Dibuja el cuadro de preferencia
        color_preferencia = (0, 0, 255) if preferencia == "I" else (255, 0, 0)
        pygame.draw.rect(pantalla, color_preferencia, [ANCHO // 2 - 50, 10, 200, 40])
        texto_preferencia = fuente.render(" PREFERENCIA ", True, BLANCO)
        pantalla.blit(texto_preferencia, [ANCHO // 2 - 45, 15])

        # Añadir coches aleatoriamente (con límite de espera)
        if random.randint(0, 150) == 0 and len(coches_izquierda) < MAX_AUTOS:
            coches_izquierda.append(Coche("I"))
            if(len(coches_derecha)==0): preferencia="I"
            

        if random.randint(0, 150) == 0 and len(coches_derecha) < MAX_AUTOS:
            coches_derecha.append(Coche("D"))
            if(len(coches_izquierda)==0): preferencia="D"    
            

        # Mover coches en el puente
        for coche in puente:
            coche.mover()
            if coche.direccion == "I" and coche.x > ANCHO:
                puente.remove(coche)
            elif coche.direccion == "D" and coche.x < 0:
                puente.remove(coche)

        # Dibujar coches
        for coche in coches_izquierda + coches_derecha + puente:
            coche.dibujar(pantalla)

        pygame.display.flip()
        reloj.tick(30)

    pygame.quit()

if __name__ == "__main__":
    main()
