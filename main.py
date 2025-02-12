import pygame
import constantes_del_juego
from personaje import Personaje

# Inicializa el personaje en una posición específica
jugador_princ = Personaje(x=350, y=50)

pygame.init()

# Configuración de la ventana
ventana = pygame.display.set_mode((constantes_del_juego.ANCHO_VENTANA, constantes_del_juego.ALTO_VENTANA))
pygame.display.set_caption("MIND FEASTABLES") # Nombre del juego.

Reloj = pygame.time.Clock() # FPS del juego

# Bucle principal del juego
run = True
while run == True:
    Reloj.tick(constantes_del_juego.FPS) # FPS del juego
    ventana.fill(constantes_del_juego.COLOR_BG)  # Limpia la pantalla con color    
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
    jugador_princ.dibujar(ventana) # Dibujar el personaje en la ventana
    pygame.display.update()  # Actualiza la pantalla
    
pygame.quit()