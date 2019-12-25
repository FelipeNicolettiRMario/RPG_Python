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

    arrayDice = []
    for i in range(2):
        dice = Azeroth.setDices()
        arrayDice.append(dice)

    print(Azeroth.rollDIce(arrayDice))
    print(Azeroth.players)