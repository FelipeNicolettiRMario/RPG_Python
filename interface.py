from character import Character as ch 
from board import Board as bd 

def crateChar(inpBoard):
    name = input("Type the name of the character: ")
    race = input("Type the race of the character: ")
    clas = input("Type the class of the character: ")
    health = input("Type the health of the character: ")

    newChar = ch(name,race,clas,health)
    inpBoard.addPlayer(newChar)

    continueAdd = input("Do you want add new chars(yes or no)? ")

    if continueAdd.lower() == "yes":
        crateChar(inpBoard)

    else:
        boards.append(inpBoard)
        main()
        

def createBoard():
    name = input("Type the name of the board: ")
    newBoard = bd(name)

    addChars = input("Do yo want add characters to this board(yes or no please)?")

    if addChars.lower() == "yes":
        crateChar(newBoard)
    else:
        boards.append(newBoard)
        main()

def getBoards():
    print("----------------------------------------")
    for board in boards:
        print(board.name)
    print("----------------------------------------")
    main()

def main():
    answer = input("Please input the what you wanna do: \n a)Create a table \n b)View my boards \n")

    if answer.lower() == "a":
        createBoard()

    elif answer.lower() == "b":
        getBoards()

if __name__ == "__main__":
    print("Welcome to Python RPG!\n")
    boards = []
    main()
