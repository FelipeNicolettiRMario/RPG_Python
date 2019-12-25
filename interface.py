from character import Character as ch 
from board import Board as bd
import random

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

    addChars = input("Do yo want add characters to this board(yes or no )?")

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

def findBoard(name):
    for board in boards:
        if board.name == name:
            return board
        else:
            print("Board not found")
            return main()

def playBoard(board):
    answer = input("Please input the what you wanna do: \n a)Add a character in the table \n b)Roll dices \n c)Show table backlog")

    if answer.lower() == "a":
        name = input("Type the name of the character: ")
        race = input("Type the race of the character: ")
        clas = input("Type the class of the character: ")
        health = input("Type the health of the character: ")

        newChar = ch(name,race,clas,health)
        board.addPLayer(newChar)

        playBoard()

    elif answer.lower() == "b":
        numberOfDices = input("How many dices you wanna roll? ")

        arrayDices = []
        for number in range(int(numberOfDices)):
            dice = board.setDices()
            arrayDices.append(dice)

        diceResults = board.rollDice(arrayDices)

        print("Results:")
        for result in diceResults:
            print(result)



def main():
    answer = input("Please input the what you wanna do: \n a)Create a table \n b)View my boards \n c)Play in a board")

    if answer.lower() == "a":
        createBoard()

    elif answer.lower() == "b":
        getBoards()

    elif answer.lower() == "c":
        name = input("Type the name of the board: ")
        board = findBoard(name)
        playBoard(board)

if __name__ == "__main__":
    print("Welcome to Python RPG!\n")
    boards = []
    main()
