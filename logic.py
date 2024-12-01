import pygame
from gadgets import SQUARE_SIZE as square_size
def handle_events(board, selected_piece, turn):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False, selected_piece, turn  # Terminar el juego

        elif event.type == pygame.MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()
            row, col = y // square_size, x // square_size
            piece = board.get_piece(row, col)
            if piece and piece.color == turn:
                selected_piece = piece

        elif event.type == pygame.MOUSEBUTTONUP and selected_piece:
            x, y = pygame.mouse.get_pos()
            new_row, new_col = y // square_size, x // square_size
            if board.move_piece(selected_piece, new_row, new_col):
                # Cambiar turno después de un movimiento válido
                turn = (0, 0, 0) if turn == (255, 255, 255) else (255, 255, 255)
            selected_piece = None

    return True, selected_piece, turn