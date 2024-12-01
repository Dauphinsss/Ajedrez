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

    def draw(self, drawer):
        drawer.draw_piece(self)