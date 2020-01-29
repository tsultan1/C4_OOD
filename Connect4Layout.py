'''
inherits from Game class with all the instance methods to create the 2D grid and player's moves on the on the screen
prints the board every time a move has been made by a player
'''

import numpy as np
import pygame

from GameRoot import Game


class connect4(Game):

    def __init__(self):
        super().__init__()

    def create_board(self):
        board = np.zeros((Game.ROW_COUNT, Game.COLUMN_COUNT))
        return board

    def evaluate_window(self, window, piece):
        score = 0
        opp_piece = Game.PLAYER_PIECE
        if piece == Game.PLAYER_PIECE:
            opp_piece = Game.AI_PIECE

        if window.count(piece) == 4:
            score += 100
        elif window.count(piece) == 3 and window.count(Game.EMPTY) == 1:
            score += 5
        elif window.count(piece) == 2 and window.count(Game.EMPTY) == 2:
            score += 2

        if window.count(opp_piece) == 3 and window.count(Game.EMPTY) == 1:
            score -= 4

        return score

    def draw_board(self, board):
        for c in range(Game.COLUMN_COUNT):
            for r in range(Game.ROW_COUNT):
                pygame.draw.rect(Game.screen, Game.BLUE,
                                 (c * Game.SQUARESIZE, r * Game.SQUARESIZE + Game.SQUARESIZE, Game.SQUARESIZE, Game.SQUARESIZE))
                pygame.draw.circle(Game.screen, Game.BLACK, (
                    int(c * Game.SQUARESIZE + Game.SQUARESIZE / 2), int(r * Game.SQUARESIZE + Game.SQUARESIZE + Game.SQUARESIZE / 2)), Game.RADIUS)

        for c in range(Game.COLUMN_COUNT):
            for r in range(Game.ROW_COUNT):
                if board[r][c] == Game.PLAYER_PIECE:
                    pygame.draw.circle(Game.screen, Game.RED, (
                        int(c * Game.SQUARESIZE + Game.SQUARESIZE / 2), Game.height - int(r * Game.SQUARESIZE + Game.SQUARESIZE / 2)), Game.RADIUS)
                elif board[r][c] == Game.AI_PIECE:
                    pygame.draw.circle(Game.screen, Game.YELLOW, (
                        int(c * Game.SQUARESIZE + Game.SQUARESIZE / 2), Game.height - int(r * Game.SQUARESIZE + Game.SQUARESIZE / 2)), Game.RADIUS)
        pygame.display.update()

    def score_position(self, board, piece):
        score = 0

        ## Score center column
        center_array = [int(i) for i in list(board[:, Game.COLUMN_COUNT // 2])]
        center_count = center_array.count(piece)
        score += center_count * 3

        ## Score Horizontal
        for r in range(Game.ROW_COUNT):
            row_array = [int(i) for i in list(board[r, :])]
            for c in range(Game.COLUMN_COUNT - 3):
                window = row_array[c:c + Game.WINDOW_LENGTH]
                score += self.evaluate_window(window, piece)

        ## Score Vertical
        for c in range(Game.COLUMN_COUNT):
            col_array = [int(i) for i in list(board[:, c])]
            for r in range(Game.ROW_COUNT - 3):
                window = col_array[r:r + Game.WINDOW_LENGTH]
                score += self.evaluate_window(window, piece)

        ## Score posiive sloped diagonal
        for r in range(Game.ROW_COUNT - 3):
            for c in range(Game.COLUMN_COUNT - 3):
                window = [board[r + i][c + i] for i in range(Game.WINDOW_LENGTH)]
                score += self.evaluate_window(window, piece)

        for r in range(Game.ROW_COUNT - 3):
            for c in range(Game.COLUMN_COUNT - 3):
                window = [board[r + 3 - i][c + i] for i in range(Game.WINDOW_LENGTH)]
                score += self.evaluate_window(window, piece)

        return score

    def print_board(self, board):
        print(np.flip(board, 0))

