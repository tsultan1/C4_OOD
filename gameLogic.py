'''
this class contains all the instance methods for the player to choose a move
'''

import random
from Connect4Layout import connect4
from GameRoot import Game


class gameLogic(connect4):
    def __init__(self):
        super().__init__()

    def drop_piece(self, board, row, col, piece):
        board[row][col] = piece

    def is_valid_location(self, board, col):
        return board[Game.ROW_COUNT - 1][col] == 0

    def get_next_open_row(self, board, col):
        for r in range(Game.ROW_COUNT):
            if board[r][col] == 0:
                return r

    def winning_move(self, board, piece):
        # Check horizontal locations for win
        for c in range(Game.COLUMN_COUNT - 3):
            for r in range(Game.ROW_COUNT):
                if board[r][c] == piece and board[r][c + 1] == piece and board[r][c + 2] == piece and board[r][
                    c + 3] == piece:
                    return True

        # Check vertical locations for win
        for c in range(Game.COLUMN_COUNT):
            for r in range(Game.ROW_COUNT - 3):
                if board[r][c] == piece and board[r + 1][c] == piece and board[r + 2][c] == piece and board[r + 3][
                    c] == piece:
                    return True

        # Check positively sloped diaganols
        for c in range(Game.COLUMN_COUNT - 3):
            for r in range(Game.ROW_COUNT - 3):
                if board[r][c] == piece and board[r + 1][c + 1] == piece and board[r + 2][c + 2] == piece and \
                        board[r + 3][
                            c + 3] == piece:
                    return True

        # Check negatively sloped diaganols
        for c in range(Game.COLUMN_COUNT - 3):
            for r in range(3, Game.ROW_COUNT):
                if board[r][c] == piece and board[r - 1][c + 1] == piece and board[r - 2][c + 2] == piece and \
                        board[r - 3][
                            c + 3] == piece:
                    return True

    def is_terminal_node(self, board):
        return self.winning_move(board, Game.PLAYER_PIECE) or self.winning_move(board, Game.AI_PIECE) or len(
            self.get_valid_locations(board)) == 0

    def get_valid_locations(self, board):
        valid_locations = []
        for col in range(Game.COLUMN_COUNT):
            if self.is_valid_location(board, col):
                valid_locations.append(col)
        return valid_locations

    def pick_best_move(self, board, piece):
        valid_locations = self.get_valid_locations(board)
        best_score = -10000
        best_col = random.choice(valid_locations)
        for col in valid_locations:
            row = self.get_next_open_row(board, col)
            temp_board = board.copy()
            self.drop_piece(temp_board, row, col, piece)
            score = self.score_position(temp_board, piece)
            if score > best_score:
                best_score = score
                best_col = col

        return best_col

