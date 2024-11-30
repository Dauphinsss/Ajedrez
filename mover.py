import pygame
import sys
MEDIUM_GRAY = (128, 128, 128)
# Configuración básica
ANCHO, ALTO = 800, 800
FILAS, COLUMNAS = 8, 8
TAMAÑO_CASILLA = ANCHO // COLUMNAS
BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0)
ROJO = (255, 0, 0)
AZUL = (0, 0, 255)

class Piece:
    def __init__(self, fila, col, color, es_reina=False):
        self.fila = fila
        self.col = col
        self.color = color
        self.es_reina = es_reina
        self.FILLED = 13
        self.CONTORN = 2
    def convertir_en_reina(self):
        self.es_reina = True


class Board:
    def __init__(self):
        self.piezas = self.colocar_piezas()

    def dibujar_tablero(self, ventana):
        ventana.fill(BLANCO)
        for fila in range(FILAS):
            for col in range(COLUMNAS):
                if (fila + col) % 2 != 0:
                    pygame.draw.rect(ventana, (60,60,60), 
                                     (col * TAMAÑO_CASILLA, fila * TAMAÑO_CASILLA, 
                                      TAMAÑO_CASILLA, TAMAÑO_CASILLA))

    def colocar_piezas(self):
        piezas = []
        for fila in range(3):
            for col in range(COLUMNAS):
                if (fila + col) % 2 != 0:
                    piezas.append(Piece(fila, col, (255,255,255)))
        for fila in range(5, 8):
            for col in range(COLUMNAS):
                if (fila + col) % 2 != 0:
                    piezas.append(Piece(fila, col, (0,0,0)))
        return piezas

    def dibujar_piezas(self, ventana):
        for pieza in self.piezas:
            pieza.dibujar(ventana)

    def obtener_pieza(self, fila, col):
        for pieza in self.piezas:
            if pieza.fila == fila and pieza.col == col:
                return pieza
        return None

    def mover_pieza(self, pieza, nueva_fila, nueva_columna):
        pieza_comida = self.puede_comer(pieza, nueva_fila, nueva_columna)
        if self.movimiento_valido(pieza, nueva_fila, nueva_columna):
            pieza.fila, pieza.col = nueva_fila, nueva_columna
            

            if pieza.color == (255,255,255) and nueva_fila == FILAS - 1:
                pieza.convertir_en_reina()
            elif pieza.color == (0,0,0) and nueva_fila == 0:
                pieza.convertir_en_reina()
                

            if pieza_comida:
                self.piezas.remove(pieza_comida)
            return True
        return False

    def movimiento_valido(self, pieza, nueva_fila, nueva_columna):
        if not (0 <= nueva_fila < FILAS and 0 <= nueva_columna < COLUMNAS):
            return False  

        if self.obtener_pieza(nueva_fila, nueva_columna) is not None:
            return False

        delta_fila = nueva_fila - pieza.fila
        delta_col = nueva_columna - pieza.col

        if abs(delta_fila) == 1 and abs(delta_col) == 1:
 
            if (pieza.color == (255,255,255) and delta_fila == 1) or (pieza.color == (0,0,0) and delta_fila == -1) or pieza.es_reina:
                return True

        elif abs(delta_fila) == 2 and abs(delta_col) == 2:
            # Movimiento de captura
            return self.puede_comer(pieza, nueva_fila, nueva_columna) is not None

        return False

    def puede_comer(self, pieza, nueva_fila, nueva_columna):
        delta_fila = (nueva_fila - pieza.fila) // 2
        delta_col = (nueva_columna - pieza.col) // 2
        fila_enemiga = pieza.fila + delta_fila
        col_enemiga = pieza.col + delta_col
        pieza_enemiga = self.obtener_pieza(fila_enemiga, col_enemiga)
        if pieza_enemiga and pieza_enemiga.color != pieza.color:
            return pieza_enemiga
        return None

def main():
    pygame.init()
    screen = pygame.display.set_mode((ANCHO, ALTO))
    pygame.display.set_caption("Juego de Damas")
    board = Board()
    game_run(screen, board)

if __name__ == "__main__":
    main()
