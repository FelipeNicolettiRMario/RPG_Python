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