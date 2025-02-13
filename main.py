import pygame
import constantes_del_juego
from personaje import Personaje

# Inicializa el personaje en una posición específica
jugador_princ = Personaje(x=350, y=50)

pygame.init()

# Configuración de la ventana
ventana = pygame.display.set_mode((constantes_del_juego.ANCHO_VENTANA, constantes_del_juego.ALTO_VENTANA))
pygame.display.set_caption("MIND FEASTABLES") # Nombre del juego.

# definir las variables de movimiento del jugador
mover_arriba = False
mover_abajo = False
mover_izquierda = False
mover_derecha = False


reloj = pygame.time.Clock() # Crotrolar los frame rate
# Bucle principal del juego
run = True
while run == True:
    reloj.tick(constantes_del_juego.FPS)  # Controla la velocidad del juego

    # Calcular el movimiento del jugador
    delta_x = 0
    delta_y = 0

    if mover_derecha == True:
            delta_x = constantes_del_juego.VELOCIDAD

    if mover_izquierda == True:
            delta_x = -constantes_del_juego.VELOCIDAD

    if mover_arriba == True:
            delta_y = -constantes_del_juego.VELOCIDAD

    if mover_abajo == True:
            delta_y = constantes_del_juego.VELOCIDAD

    # Mover al jugador
    jugador_princ.movimiento(delta_x, delta_y)
    ventana.fill(constantes_del_juego.COLOR_BG)  # Limpia la pantalla con color    
    # Eventos del juego
    jugador_princ.dibujar(ventana)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    pygame.display.update()  # Actualiza la pantalla                    
      
                                # Eventos del teclado   
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_LEFT:
            mover_izquierda = True
        if event.key == pygame.K_RIGHT:
            mover_derecha = True    
        if event.key == pygame.K_UP:
            mover_arriba = True
        if event.key == pygame.K_DOWN:
            mover_abajo = True
    # Para cuando se selte la tecla
    if event.type == pygame.KEYUP:
        if event.key == pygame.K_LEFT:
                mover_izquierda = False
        if event.key == pygame.K_RIGHT:
                mover_derecha = False    
        if event.key == pygame.K_UP:
                mover_arriba = False
        if event.key == pygame.K_DOWN:
                mover_abajo = False
    
pygame.quit()