'''
the Game class contains all the class variables to be used by other classes
'''

import pygame


class Game:
    BLUE = (0,255,170)
    BLACK = (0, 0, 0)
    RED = (255, 0, 0)
    YELLOW = (255, 255, 0)
    ROW_COUNT = 6
    COLUMN_COUNT = 7
    EMPTY = 0
    WINDOW_LENGTH = 4
    SQUARESIZE = 80
    width = COLUMN_COUNT * SQUARESIZE
    height = (ROW_COUNT + 1) * SQUARESIZE
    size = (width, height)
    screen = pygame.display.set_mode(size)
    RADIUS = int(SQUARESIZE / 2 - 5)
    PLAYER = 0
    AI = 1
    PLAYER_PIECE = 1
    AI_PIECE = 2


def __init__(self, gameName):
    self.name = gameName
