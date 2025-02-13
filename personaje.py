import pygame
import constantes_del_juego

class Personaje():
    def __init__(self, y, x):
        self.forma = pygame.Rect(0, 0, constantes_del_juego.ANCHO_PERSONAJE, constantes_del_juego.ALTO_PERSONAJE)
        self.forma.center = (x,y)

    def movimiento(self, delta_x, delta_y):
        self.forma.x = self.forma.x + delta_x
        self.forma.y = self.forma.y + delta_y

    def dibujar(self, interfaz):
        pygame.draw.rect(interfaz, constantes_del_juego.COLOR_PERSONAJE, self.forma)

         
