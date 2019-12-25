import random

class Board:
    
    def __init__(self,name):
        self.name = name
        self.players = []
        self.backlog = []

    def addPlayer(self,player):
        self.players.append(player)
    
    def addBacklog(self,message):
        self.backlog.append(message)

    def removePlayer(self,name):

        tbdPlayers = self.players.copy()
        for player in self.players:
            if player.name == name:
                playerIndex = self.players.index(player)
                tbdPlayers.pop(playerIndex)
    
        self.players = tbdPlayers
    
    def rollDIce(self,dices):
        returnedValues = []
        for dice in dices:
            maxVal = dice['Faces']
            roll = random.randint(1,int(maxVal))
            for values in dice['Modifiers']:
                roll += values
            returnedValues.append(roll)
        return returnedValues

    def setDices(self):
        faces = input("Type the number of faces of the dice: ")
        modifiersCheck = input("Do you want to add modifiers to the dice?")

        modifiers = []
        if modifiersCheck.lower() == "yes":
            modifiersNumbers = input("Type the number of modifiers")

            for number in range(int(modifiersNumbers)):
                modifier = input("Type the mofifier: ")
                modifiers.append(int(modifier))

        diceDict = {"Faces":faces,"Modifiers":modifiers}

        return diceDict

