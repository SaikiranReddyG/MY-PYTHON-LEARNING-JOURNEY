from constant import *
from square import Square
from Piece import *
from move import Move


class Board:

    def __init__(self):
        self.squares = [[0, 0, 0, 0, 0, 0, 0, 0] for col in range(COLS)]

        self._create()
        self._add_pieces('white')
        self._add_pieces('black')

    def calc_moves(self, Piece, row, col):
        """"calculate all the possible moves of a specific piece position"""

        def Pawn_moves():
            """steps"""
            steps = 1 if Piece.moved else 2

            # vertical moves
            start = row + Piece.dir
            end = row + (Piece.dir * (1 + steps))
            for possible_move_row in range(start, end, Piece.dir):
                if Square.in_range(possible_move_row):
                    if self.squares[possible_move_row][col].is_empty():
                        # create initial and final moves
                        initial = Square(row, col)
                        final = Square(possible_move_row, col)
                        # create a new move
                        move = Move(initial, final)
                        Piece.add_move(move)

                    else: break
                else: break

            # diagonal moves
            possible_move_row = row + Piece.dir
            possible_move_cols = (col - 1, col + 1)
            for possible_move_cols in possible_move_cols:
                if Square.in_range(possible_move_row, possible_move_cols):
                    if self.squares[possible_move_row][possible_move_cols].has_enemy_piece(Piece.color):
                        initial = Square(row, col)
                        final = Square(possible_move_row, possible_move_cols)
                        Piece.add_move(move)



        def knight_moves():
            # 8 possible moves
            possible_moves = [
                (row-2, col+1),
                (row-1, col+2),
                (row+1, col+2),
                (row+2, col+1),
                (row+2, col-1),
                (row+1, col-2),
                (row-1, col-2),
                (row-2, col-1),
            ]
            for possible_move in possible_moves:
                possible_move_row, possible_move_col = possible_move

                if Square.in_range(possible_move_row, possible_move_col):
                    if self.squares[possible_move_row][possible_move_col].isempty_or_enemy(Piece.color):
                        """ create squares of the new move """
                        initial = Square(row, col)
                        final = Square(possible_move_row, possible_move_col)
                        """create new move"""
                        move = Move(initial, final)
                        """append new valid move"""
                        Piece.add_move(move)

        def stright_line_moves(incrs):
            for incr in incrs:
                row_incr, col_incr = incr
                possible_move_row = row + row_incr
                possible_move_col = col + col_incr

                while True:
                    if Square.in_range(possible_move_row, possible_move_col):
                        # create squares of the possible new move
                        initial = Square(row, col)
                        final = Square(possible_move_row, possible_move_col)
                        # create a possible new move
                        move = Move(initial, final)
                        # empty
                        if self.squares[possible_move_row][possible_move_col].isempty():
                            # append new move
                            Piece.add_move(move)

                        # has empty piece
                        if self.squares[possible_move_row][possible_move_col].has_enemy_piece(Piece.color):
                            # append new move
                            Piece.add_move(move)
                            break

                        # team piece
                        if self.squares[possible_move_row][possible_move_col].has_team_piece(Piece.color):
                            break

                    else:
                        break
                    # incrementing incrs
                    possible_move_row = possible_move_row + row_incr
                    possible_move_col = possible_move_col + col_incr

        if isinstance(Piece, Pawn):
            Pawn_moves()

        elif isinstance(Piece, Knight):
            knight_moves()

        elif isinstance(Piece, Bishop):
            stright_line_moves([(-1, 1), # up-right
                                (-1, -1), # up-left
                                (1, 1), # down - right
                                (1, -1), # down - left
                                ])

        elif isinstance(Piece, Rook):
            stright_line_moves([
                (-1, 0), # up
                (0, 1), # right
                (1, 0), # down
                (0, -1), # left
            ])

        elif isinstance(Piece, Queen):
            stright_line_moves(([(-1, 1), # up-right
                                (-1, -1), # up-left
                                (1, 1), # down - right
                                (1, -1),
                                (-1, 0),
                                (0, 1),
                                (1, 0),
                                (0, -1),
                                ]))

        elif isinstance(Piece, King): pass


    def _create(self):
        for row in range(ROWS):
            for col in range(COLS):
                self.squares[row][col] = Square(row, col)

    def _add_pieces(self, color):
        row_pawn, row_other = (6, 7) if color == 'white' else (1, 0)

        # pawns
        for col in range(COLS):
            self.squares[row_pawn][col] = Square(row_pawn, col, Pawn(color))

        # knights
        self.squares[row_other][1] = Square(row_other, 1, Knight(color))
        self.squares[row_other][6] = Square(row_other, 6, Knight(color))

        # bishops
        self.squares[row_other][2] = Square(row_other, 2, Bishop(color))
        self.squares[row_other][5] = Square(row_other, 5, Bishop(color))

        # rooks
        self.squares[row_other][0] = Square(row_other, 0, Rook(color))
        self.squares[row_other][7] = Square(row_other, 7, Rook(color))

        # queen
        self.squares[row_other][3] = Square(row_other, 3, Queen(color))

        # king
        self.squares[row_other][4] = Square(row_other, 4, King(color))
