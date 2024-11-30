import pygame
import unittest
from runner import game_run
from board import Board
from piece import Piece
from gadgets import LIGHT_GRAY, BLACK

class TestCheckers(unittest.TestCase):
    
    def setUp(self):
        pygame.init()
        self.screen = pygame.display.set_mode((800, 800))
        self.board = Board()

    def tearDown(self):
        pygame.quit()
    
    def test_obtener_pieza(self):
        # Verifica que obtener_pieza devuelva la pieza correcta o None si no hay pieza
        pieza = self.board.obtener_pieza(0, 1)
        self.assertIsNotNone(pieza, "Se espera una pieza en la posición (0, 1)")
        self.assertEqual(pieza.color, (255, 255, 255), "La pieza en (0, 1) debería ser blanca")
        self.assertIsNone(self.board.obtener_pieza(0, 0), "No debería haber pieza en (0, 0)")

    def test_mover_pieza_valido(self):
        # Prueba que el método mover_pieza funcione con un movimiento válido
        pieza = self.board.obtener_pieza(2, 1)
        resultado = self.board.mover_pieza(pieza, 3, 2)
        self.assertTrue(resultado, "El movimiento debería ser válido")
        self.assertEqual((pieza.row, pieza.col), (3, 2), "La pieza debería estar en la posición (3, 2)")

    def test_mover_pieza_invalido(self):
        # Prueba que un movimiento inválido no se realice
        pieza = self.board.obtener_pieza(2, 1)
        resultado = self.board.mover_pieza(pieza, 5, 5)
        self.assertFalse(resultado, "El movimiento debería ser inválido")
        self.assertEqual((pieza.row, pieza.col), (2, 1), "La pieza debería seguir en (2, 1)")

    def test_movimiento_y_captura(self):
        # Coloca una pieza negra para capturar y verifica el resultado
        pieza_blanca = self.board.obtener_pieza(2, 1)
        pieza_negra = Piece(3, 2, (0, 0, 0))
        self.board.piezas.append(pieza_negra)
        resultado = self.board.mover_pieza(pieza_blanca, 4, 3)
        self.assertTrue(resultado, "El movimiento debería ser válido con captura")
        self.assertNotIn(pieza_negra, self.board.piezas, "La pieza negra debería ser removida")

    def test_promocion_a_reina(self):
        # Verifica que una pieza blanca se convierta en reina al alcanzar el extremo
        pieza = self.board.obtener_pieza(6, 1)
        self.board.piezas.remove(pieza)
        pieza = self.board.obtener_pieza(7, 0)
        self.board.piezas.remove(pieza)
        pieza= Piece(6,1,(255,255,255))
        self.board.mover_pieza(pieza, 7, 0)
        self.assertTrue(pieza.king, "La pieza debería ser una reina")

    def test_dibujar_tablero(self):
        # Prueba que el método dibujar_tablero no cause errores
        try:
            self.board.dibujar_tablero(self.screen)
            success = True
        except Exception:
            success = False
        self.assertTrue(success, "El tablero debería dibujarse sin errores")

    def test_dibujar_piezas(self):
        # Prueba que el método dibujar_piezas no cause errores
        try:
            self.board.dibujar_piezas(self.screen)
            success = True
        except Exception:
            success = False
        self.assertTrue(success, "Las piezas deberían dibujarse sin errores")

if __name__ == '__main__':
    unittest.main()