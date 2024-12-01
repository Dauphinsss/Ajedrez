import pygame
import sys
from logic import handle_events
from drawer import Drawer

def game_run(screen, board):
    drawer = Drawer(screen)
    selected_piece = None
    running = True
    turn = (255, 255, 255)

    while running:
        board.draw_board(drawer)
        board.draw_pieces(drawer)
        pygame.display.flip()

        running, selected_piece, turn = handle_events(board, selected_piece, turn)
        if not running:
            pygame.quit()
            sys.exit()