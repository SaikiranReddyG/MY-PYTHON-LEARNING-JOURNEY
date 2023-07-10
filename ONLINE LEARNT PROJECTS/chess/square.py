class Square:

    def __init__(self, row, col, piece=None):
        self.row = row
        self.col = col
        self.Piece = piece

    def has_piece(self):
        return self.Piece != None

    def is_empty(self):
        return not self.has_piece()

    def has_team_piece(self, color):
        return self.has_piece() and self.Piece.color == color

    def has_enemy_piece(self, color):
        return self.has_piece() and self.Piece.color != color

    def isempty_or_enemy(self, color):
        return self.is_empty() or self.has_enemy_piece(color)

    @staticmethod
    def in_range(*args):
        for arg in args:
            if arg < 0 or arg > 7:
                return False

        return True
