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
    
    def test_get_piece(self):
        # Verifies that get_piece returns the correct piece or None if there is no piece
        piece = self.board.get_piece(0, 1)
        self.assertIsNotNone(piece, "A piece is expected at position (0, 1)")
        self.assertEqual(piece.color, (255, 255, 255), "The piece at (0, 1) should be white")
        self.assertIsNone(self.board.get_piece(0, 0), "There should be no piece at (0, 0)")

    def test_move_piece_valid(self):
        # Tests that the move_piece method works with a valid move
        piece = self.board.get_piece(2, 1)
        result = self.board.move_piece(piece, 3, 2)
        self.assertTrue(result, "The move should be valid")
        self.assertEqual((piece.row, piece.col), (3, 2), "The piece should be at position (3, 2)")

    def test_move_piece_invalid(self):
        # Tests that an invalid move does not occur
        piece = self.board.get_piece(2, 1)
        result = self.board.move_piece(piece, 5, 5)
        self.assertFalse(result, "The move should be invalid")
        self.assertEqual((piece.row, piece.col), (2, 1), "The piece should remain at (2, 1)")

    def test_move_and_capture(self):
        # Places a black piece to capture and verifies the result
        white_piece = self.board.get_piece(2, 1)
        black_piece = Piece(3, 2, (0, 0, 0))
        self.board.pieces.append(black_piece)
        result = self.board.move_piece(white_piece, 4, 3)
        self.assertTrue(result, "The move should be valid with capture")
        self.assertNotIn(black_piece, self.board.pieces, "The black piece should be removed")

    def test_promotion_to_queen(self):
        # Verifies that a white piece is promoted to a queen upon reaching the end
        piece = self.board.get_piece(6, 1)
        self.board.pieces.remove(piece)
        piece = self.board.get_piece(7, 0)
        self.board.pieces.remove(piece)
        piece = Piece(6, 1, (255, 255, 255))
        self.board.move_piece(piece, 7, 0)
        self.assertTrue(piece.king, "The piece should be a queen")

    def test_draw_board(self):
        # Tests that the draw_board method does not cause errors
        try:
            self.board.draw_board(self.screen)
            success = True
        except Exception:
            success = False
        self.assertTrue(success, "The board should be drawn without errors")

    def test_draw_pieces(self):
        # Tests that the draw_pieces method does not cause errors
        try:
            self.board.draw_pieces(self.screen)
            success = True
        except Exception:
            success = False
        self.assertTrue(success, "The pieces should be drawn without errors")

if __name__ == '__main__':
    unittest.main()
