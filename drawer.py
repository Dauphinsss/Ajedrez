import pygame
from gadgets import ROWS, COLS, SQUARE_SIZE, WHITE, MEDIUM_GRAY

class Drawer:
    def __init__(self, window):
        self.window = window

    def draw_board(self, board):
        self.window.fill(WHITE)
        for row in range(ROWS):
            for col in range(COLS):
                if (row + col) % 2 != 0:
                    pygame.draw.rect(self.window, (60, 60, 60),
                                     (col * SQUARE_SIZE, row * SQUARE_SIZE,
                                      SQUARE_SIZE, SQUARE_SIZE))

    def draw_piece(self, piece):
        radius = SQUARE_SIZE // 2 - piece.FILLED
        inner_radius = SQUARE_SIZE // 2 - piece.FILLED + 8

        pygame.draw.circle(self.window, piece.color, 
                           ((piece.col * SQUARE_SIZE) + (SQUARE_SIZE // 2),
                            (piece.row * SQUARE_SIZE) + (SQUARE_SIZE // 2)), 
                           inner_radius + piece.OUTLINE)

        pygame.draw.circle(self.window, MEDIUM_GRAY, 
                           ((piece.col * SQUARE_SIZE) + (SQUARE_SIZE // 2),
                            (piece.row * SQUARE_SIZE) + (SQUARE_SIZE // 2)), 
                           radius + piece.OUTLINE)

        pygame.draw.circle(self.window, piece.color, 
                           ((piece.col * SQUARE_SIZE) + (SQUARE_SIZE // 2),
                            (piece.row * SQUARE_SIZE) + (SQUARE_SIZE // 2)), 
                           radius)

        if piece.king:
            pygame.draw.circle(self.window, (255, 215, 0), 
                               (piece.col * SQUARE_SIZE + SQUARE_SIZE // 2,
                                piece.row * SQUARE_SIZE + SQUARE_SIZE // 2), 
                               SQUARE_SIZE // 2 - 5, 3)

    def draw_pieces(self, pieces):
        for piece in pieces:
            self.draw_piece(piece)