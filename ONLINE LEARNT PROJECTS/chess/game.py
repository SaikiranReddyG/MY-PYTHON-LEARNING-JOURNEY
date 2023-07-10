import pygame
from constant import *
from board import Board
from dragger import dragger


class Game:
    def __init__(self):
        self.board = Board()
        self.dragger = dragger()

    # blit methods
    def show_bg(self, surface):
        for row in range(ROWS):
            for col in range(COLS):
                if (row + col) % 2 == 0:
                    color = (234, 235, 200)  # light green
                else:
                    color = (119, 154, 88)  # dark green

                rect = (col * square_size, row * square_size, square_size, square_size)

                pygame.draw.rect(surface, color, rect)

    def show_pieces(self, surface):
        for row in range(ROWS):
            for col in range(COLS):
                if self.board.squares[row][col].has_piece():
                    piece = self.board.squares[row][col].Piece

                    # all pieces except dragger piece
                    if piece is not self.dragger.piece:
                        piece.set_texture(size=80)
                        img = pygame.image.load(piece.texture)
                        img_center = col * square_size + square_size // 2, row * square_size + square_size // 2
                        piece.texture_rect = img.get_rect(center=img_center)
                        surface.blit(img, piece.texture_rect)

    def show_moves(self, surface):
        if self.dragger.dragging:
            piece = self.dragger.piece

            for move in piece.moves:
                # color
                color = '#C86464' if (move.final.row + move.final.col) % 2 == 0 else '#C84646'
                # rect
                rect = (move.final.col + square_size, move.final.row + square_size, square_size, square_size)
                # blit
                pygame.draw.rect(surface, color, rect)

