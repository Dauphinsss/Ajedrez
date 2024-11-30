import pygame
import sys
from gadgets import BLACK, SQUARE_SIZE as TAMAÑO_CASILLA
from logic import handle_events


def game_run(screen, board):
    pieza_seleccionada = None
    corriendo = True
    turno = (255,255,255)

    while corriendo:
        board.dibujar_tablero(screen)
        board.dibujar_piezas(screen)
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                corriendo = False
                pygame.quit()
                sys.exit()

            elif event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                fila, col = y // TAMAÑO_CASILLA, x // TAMAÑO_CASILLA
                pieza = board.obtener_pieza(fila, col)
                if pieza and pieza.color == turno:
                    pieza_seleccionada = pieza

            elif event.type == pygame.MOUSEBUTTONUP and pieza_seleccionada:
                x, y = pygame.mouse.get_pos()
                nueva_fila, nueva_columna = y // TAMAÑO_CASILLA, x // TAMAÑO_CASILLA
                if board.mover_pieza(pieza_seleccionada, nueva_fila, nueva_columna):
                    turno = (0,0,0) if turno == (255,255,255) else (255,255,255)
                pieza_seleccionada = None
