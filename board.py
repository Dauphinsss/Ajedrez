import pygame
from gadgets import ROWS as ROWS, COLS as COLS, SQUARE_SIZE as SQUARE_SIZE, WHITE as WHITE, BLACK, GRAY, LIGHT_GRAY
from piece import Piece

class Board:
    def __init__(self):
        self.pieces = self.place_pieces()

    def draw_board(self, window):
        window.fill(WHITE)
        for row in range(ROWS):
            for col in range(COLS):
                if (row + col) % 2 != 0:
                    pygame.draw.rect(window, (60, 60, 60),
                                     (col * SQUARE_SIZE, row * SQUARE_SIZE,
                                      SQUARE_SIZE, SQUARE_SIZE))

    def place_pieces(self):
        pieces = []
        for row in range(3):
            for col in range(COLS):
                if (row + col) % 2 != 0:
                    pieces.append(Piece(row, col, (255, 255, 255)))
        for row in range(5, 8):
            for col in range(COLS):
                if (row + col) % 2 != 0:
                    pieces.append(Piece(row, col, (0, 0, 0)))
        return pieces

    def draw_pieces(self, window):
        for piece in self.pieces:
            piece.draw(window)

    def get_piece(self, row, col):
        for piece in self.pieces:
            if piece.row == row and piece.col == col:
                return piece
        return None

    def move_piece(self, piece, new_row, new_col):
        captured_piece = self.can_capture(piece, new_row, new_col)
        if not self.valid_move(piece, new_row, new_col):
            return False

        self.update_position(piece, new_row, new_col)
        self.promote_to_queen_if_applicable(piece, new_row)
        self.remove_captured_piece(captured_piece)
        return True

    def update_position(self, piece, new_row, new_col):
        piece.row, piece.col = new_row, new_col

    def promote_to_queen_if_applicable(self, piece, new_row):
        if piece.color == (255, 255, 255) and new_row == ROWS - 1:
            piece.make_queen()
        elif piece.color == (0, 0, 0) and new_row == 0:
            piece.make_queen()

    def remove_captured_piece(self, captured_piece):
        if captured_piece:
            self.pieces.remove(captured_piece)


    def valid_move(self, piece, new_row, new_col):
        if not self.is_within_bounds(new_row, new_col):
            return False
        if self.is_destination_occupied(new_row, new_col):
            return False
        delta_row, delta_col = new_row - piece.row, new_col - piece.col
        if self.is_simple_move_valid(piece, delta_row, delta_col):
            return True
        elif self.is_capture_move_valid(piece, delta_row, delta_col, new_row, new_col):
            return True

        return False

    def is_within_bounds(self, row, col):
        return 0 <= row < ROWS and 0 <= col < COLS

    def is_destination_occupied(self, row, col):
        return self.get_piece(row, col) is not None

    def is_simple_move_valid(self, piece, delta_row, delta_col):
        if abs(delta_row) == 1 and abs(delta_col) == 1:
            return (piece.color == (255, 255, 255) and delta_row == 1) or \
                (piece.color == (0, 0, 0) and delta_row == -1) or \
                piece.king
        return False

    def is_capture_move_valid(self, piece, delta_row, delta_col, new_row, new_col):
        if abs(delta_row) == 2 and abs(delta_col) == 2:
            return self.can_capture(piece, new_row, new_col) is not None
        return False

    def can_capture(self, piece, new_row, new_col):
        print(new_row, new_col)
        delta_row = (new_row - piece.row) // 2
        delta_col = (new_col - piece.col) // 2
        print(delta_row, delta_col)
        enemy_row = piece.row + delta_row
        enemy_col = piece.col + delta_col
        print(enemy_row, enemy_col)
        enemy_piece = self.get_piece(enemy_row, enemy_col)
        if enemy_piece and enemy_piece.color != piece.color:
            return enemy_piece
        return None
