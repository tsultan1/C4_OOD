'''
Player class inherits from gamelogic class with the playername and an instance method
'''

from gameLogic import gameLogic


class Player(gameLogic):

    def __init__(self, playerName):
        super().__init__()
        self.playerName = playerName

    def getPlayerName(self):
        return self.playerName
