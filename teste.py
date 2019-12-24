import character as ch
import board as bd 

if __name__ == "__main__":
    Character = ch.Character
    Board = bd.Board

    Bob = Character("Bob","Orc","Ladin",80)
    Azeroth = Board("Azeroth")

    Azeroth.addPlayer(Bob)

    Bob.setItem("Chave","Objeto","Nulo","Abre algo",1)
    Bob.setHealth("INCREASE",10)
    Bob.setHealth("DECREASE",5)
    Azeroth.removePlayer("Bob")
    
    print(Azeroth.players)