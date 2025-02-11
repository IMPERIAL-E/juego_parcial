import pygame
import constantes_del_juego
from personaje import Personaje

# Inicializa el personaje en una posición específica
jugador_princ = Personaje(x=350, y=50)

pygame.init()

# Configuración de la ventana
ventana = pygame.display.set_mode((constantes_del_juego.ANCHO_VENTANA, constantes_del_juego.ALTO_VENTANA))
pygame.display.set_caption("MIND FEASTABLES") # Nombre del juego.

# Variables de movimiento.


# Bucle principal del juego
run = True
while run == True:
    # Eventos del juego
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

            # Eventos del teclado
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT: # Si se presiona la tecla izquierda
                jugador_princ.forma.move_ip(-5, 0)
            if event.key == pygame.K_RIGHT: # Si se presiona la tecla derecha
                jugador_princ.forma.move_ip(5, 0)
            if event.key == pygame.K_UP: # Si se presiona la tecla arriba
                jugador_princ.forma.move_ip(0, -5)
            if event.key == pygame.K_DOWN: # Si se presiona la tecla de abajo
                jugador_princ.forma.move_ip(0, 5)
                
        if event.type == pygame.KEYUP: # Nuevo evento para letras sueltas
            if event.key == pygame.K_a: # Si se presiona la tecla izquierda
                jugador_princ.forma.move_ip(-5, 0)
            if event.key == pygame.K_d: # Si se presiona la tecla derecha
                jugador_princ.forma.move_ip(5, 0)
            if event.key == pygame.K_w: # Si se presiona la tecla arriba
                jugador_princ.forma.move_ip(0, -5)
            if event.key == pygame.K_s: # Si se presiona la tecla de abajo
                jugador_princ.forma.move_ip(0, 5)

    # Dibujar el personaje en la ventana
    ventana.fill((0, 0, 0))  # Limpia la pantalla con color negro
    jugador_princ.dibujar(ventana) # Dibujar el personaje en la ventana
    pygame.display.update()  # Actualiza la pantalla
    
pygame.quit()