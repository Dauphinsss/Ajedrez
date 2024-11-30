import pygame
from gadgets import ROWS as FILAS , COLS as COLUMNAS , SQUARE_SIZE as TAMAÑO_CASILLA , WHITE as BLANCO, BLACK, GRAY, LIGHT_GRAY
from piece import Piece 

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
            if pieza.row == fila and pieza.col == col:
                return pieza
        return None

    def mover_pieza(self, pieza, nueva_fila, nueva_columna):
        pieza_comida = self.puede_comer(pieza, nueva_fila, nueva_columna)
        if self.movimiento_valido(pieza, nueva_fila, nueva_columna):
            pieza.row, pieza.col = nueva_fila, nueva_columna
            

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
        delta_fila = nueva_fila - pieza.row
        delta_col = nueva_columna - pieza.col
        
        if abs(delta_fila) == 1 and abs(delta_col) == 1:
 
            if (pieza.color == (255,255,255) and delta_fila == 1) or (pieza.color == (0,0,0) and delta_fila == -1) or pieza.king:
                return True

        elif abs(delta_fila) == 2 and abs(delta_col) == 2:
            # Movimiento de captura
            return self.puede_comer(pieza, nueva_fila, nueva_columna) is not None

        return False

    def puede_comer(self, pieza, nueva_fila, nueva_columna):
        print (nueva_fila,nueva_columna)
        delta_fila = (nueva_fila - pieza.row) // 2
        delta_col = (nueva_columna - pieza.col) // 2
        print (delta_fila,delta_col)
        fila_enemiga = pieza.row + delta_fila
        col_enemiga = pieza.col + delta_col
        print (fila_enemiga,fila_enemiga)
        pieza_enemiga = self.obtener_pieza(fila_enemiga, col_enemiga)
        if pieza_enemiga and pieza_enemiga.color != pieza.color:
            return pieza_enemiga
        return None
    