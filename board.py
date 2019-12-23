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
        self.players.remove(name)
    
