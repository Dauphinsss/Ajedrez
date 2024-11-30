import pygame
from gadgets import SQUARE_SIZE as SQUARE_SIZE, MEDIUM_GRAY, SQUARE_SIZE

class Piece:
    FILLED = 13
    OUTLINE = 2

    def __init__(self, row, col, color):
        self.row = row
        self.col = col
        self.color = color
        self.king = False

    def make_queen(self):
        self.king = True

    def draw(self, window):
        radius = SQUARE_SIZE // 2 - self.FILLED
        inner_radius = SQUARE_SIZE // 2 - self.FILLED + 8

        pygame.draw.circle(window, self.color, ((self.col * SQUARE_SIZE) + (SQUARE_SIZE // 2),
                                                (self.row * SQUARE_SIZE) + (SQUARE_SIZE // 2)), 
                           inner_radius + self.OUTLINE)

        pygame.draw.circle(window, MEDIUM_GRAY, ((self.col * SQUARE_SIZE) + (SQUARE_SIZE // 2),
                                                 (self.row * SQUARE_SIZE) + (SQUARE_SIZE // 2)), 
                           radius + self.OUTLINE)

        pygame.draw.circle(window, self.color, ((self.col * SQUARE_SIZE) + (SQUARE_SIZE // 2),
                                                (self.row * SQUARE_SIZE) + (SQUARE_SIZE // 2)), 
                           radius)

        if self.king:
            pygame.draw.circle(window, (255, 215, 0), 
                               (self.col * SQUARE_SIZE + SQUARE_SIZE // 2,
                                self.row * SQUARE_SIZE + SQUARE_SIZE // 2), 
                               SQUARE_SIZE // 2 - 5, 3)
