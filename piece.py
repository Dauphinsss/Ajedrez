import pygame
from gadgets import SQUARE_SIZE as TAMAÑO_CASILLA, MEDIUM_GRAY, SQUARE_SIZE

class Piece:
    FILLED = 13
    CONTORN = 2
    def __init__(self, row, col, color):
        self.row = row
        self.col = col
        self.color = color
        self.king = False
    def convertir_en_reina(self):
        self.king = True
    
    def dibujar(self, ventana):
        radius = TAMAÑO_CASILLA//2 - self.FILLED
        interior =TAMAÑO_CASILLA//2 -self.FILLED + 8
        
            
        pygame.draw.circle(ventana, self.color, ((self.col*TAMAÑO_CASILLA)+(TAMAÑO_CASILLA//2),
                                                (self.row*TAMAÑO_CASILLA)+(TAMAÑO_CASILLA//2)), interior+self.CONTORN)
        
        pygame.draw.circle(ventana, MEDIUM_GRAY, ((self.col*TAMAÑO_CASILLA)+(TAMAÑO_CASILLA//2),
                                           (self.row*TAMAÑO_CASILLA)+(TAMAÑO_CASILLA//2)), radius+self.CONTORN)
        pygame.draw.circle(ventana,self.color, ((self.col*TAMAÑO_CASILLA)+(TAMAÑO_CASILLA//2),
                                                (self.row*TAMAÑO_CASILLA)+(TAMAÑO_CASILLA//2)), radius)
        if self.king:
            pygame.draw.circle(ventana, (255, 215, 0), 
                               (self.col * TAMAÑO_CASILLA + TAMAÑO_CASILLA // 2,
                                self.row * TAMAÑO_CASILLA + TAMAÑO_CASILLA // 2), 
                               TAMAÑO_CASILLA // 2 - 5, 3)
