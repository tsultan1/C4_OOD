'''
main class runs as long as player does not choose to exit out or the game is over
'''

import math
import sys
import random
import pygame
from CPAI import CP
from Connect4Layout import connect4
from GameRoot import Game
from gameLogic import gameLogic


def main():
    GameObject = Game()
    createGame = connect4()
    board = createGame.create_board()
    logic = gameLogic()
    createGame.create_board()
    AI = CP()

    createGame.print_board(board)
    game_over = False

    pygame.init()

    createGame.draw_board(board)
    pygame.display.update()

    myfont = pygame.font.SysFont("monospace", 75)

    turn = random.randint(Game.PLAYER, Game.AI)

    while not game_over:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            if event.type == pygame.MOUSEMOTION:
                pygame.draw.rect(GameObject.screen, GameObject.BLACK, (0, 0, GameObject.width, GameObject.SQUARESIZE))
                posx = event.pos[0]
                if turn == GameObject.PLAYER:
                    pygame.draw.circle(Game.screen, Game.RED, (posx, int(Game.SQUARESIZE / 2)), Game.RADIUS)

            pygame.display.update()

            if event.type == pygame.MOUSEBUTTONDOWN:
                pygame.draw.rect(Game.screen, Game.BLACK, (0, 0, Game.width, Game.SQUARESIZE))
                # print(event.pos)
                # Ask for Player 1 Input
                if turn == Game.PLAYER:
                    posx = event.pos[0]
                    col = int(math.floor(posx / Game.SQUARESIZE))

                    if logic.is_valid_location(board, col):
                        row = logic.get_next_open_row(board, col)
                        logic.drop_piece(board, row, col, Game.PLAYER_PIECE)

                        if logic.winning_move(board, Game.PLAYER_PIECE):
                            label = myfont.render("You Win!", 1, Game.RED)
                            print("*******You beat AI!*******")
                            Game.screen.blit(label, (40, 10))
                            game_over = True

                        turn += 1
                        turn = turn % 2

                        createGame.print_board(board)
                        createGame.draw_board(board)

        # # Ask for Player 2 Input
        if turn == Game.AI and not game_over:

            # col = random.randint(0, COLUMN_COUNT-1)
            # col = logic.pick_best_move(board, Game.AI_PIECE)
            col, minimax_score = AI.minimax(board, 5, -math.inf, math.inf, True)

            if logic.is_valid_location(board, col):
                # pygame.time.wait(500)
                row = logic.get_next_open_row(board, col)
                logic.drop_piece(board, row, col, Game.AI_PIECE)

                if logic.winning_move(board, Game.AI_PIECE):
                    label = myfont.render("You lose!", 1, Game.YELLOW)
                    print("******You Lose!******")
                    Game.screen.blit(label, (40, 10))
                    game_over = True

                createGame.print_board(board)
                createGame.draw_board(board)
                print("--------Current Round--------")

                turn += 1
                turn = turn % 2

        if game_over:
            pygame.time.wait(8000)


if __name__ == '__main__':
    main()
