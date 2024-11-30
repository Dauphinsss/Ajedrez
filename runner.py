import pygame
import sys
from gadgets import BLACK, SQUARE_SIZE as SQUARE_SIZE
from logic import handle_events

def game_run(screen, board):
    selected_piece = None
    running = True
    turn = (255, 255, 255)

    while running:
        board.draw_board(screen)
        board.draw_pieces(screen)
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                sys.exit()

            elif event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                row, col = y // SQUARE_SIZE, x // SQUARE_SIZE
                piece = board.get_piece(row, col)
                if piece and piece.color == turn:
                    selected_piece = piece

            elif event.type == pygame.MOUSEBUTTONUP and selected_piece:
                x, y = pygame.mouse.get_pos()
                new_row, new_col = y // SQUARE_SIZE, x // SQUARE_SIZE
                if board.move_piece(selected_piece, new_row, new_col):
                    turn = (0, 0, 0) if turn == (255, 255, 255) else (255, 255, 255)
                selected_piece = None
