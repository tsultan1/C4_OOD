'''
Human class inherits from the Player class
'''

from Player import Player


class Human(Player):

    def __init__(self, playerName):
        super().__init__(playerName)

