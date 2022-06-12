from random import randint

totalPieces = randint(80, 100)
turn = randint(0, 1)


def titleScreen():
    print("-----------------------------------------------------------------------------------------------------")
    beginning = input(
        "Hello, and welcome to the game of NIM! Press E to start and R to read the rules (E/R)")

    if beginning == "R":
        print("-----------------------------------------------------------------------------------------------------")
        print("At the beginning of each game, there will be a random amount of pieces.")
        print(
            "Each player will take turns taking a number of pieces out of the total pieces. This number cannot exceed half of the remaining pieces")
        print(
            "The objective of the game is to not be the person to take out the last piece. If you are this person, you lose. Have fun!")

        titleScreen()
    if beginning == "E":
        startGame()


def startGame():
    global turn
    if turn == 0:
        playerTurn()
    elif turn == 1:
        computerTurn()


def playerTurn():
    global totalPieces
    global turn
    print("-----------------------------------------------------------------------------------------------------")
    print("It is your turn!")
    print("There are " + str(totalPieces) + " pieces remaining")
    takePieces = input("How many pieces do you want to take?")
    if takePieces.isnumeric() and int(takePieces) <= int(totalPieces / 2):
        print("-----------------------------------------------------------------------------------------------------")
        print("You took " + takePieces + " marbles")
        totalPieces -= int(takePieces)
    else:
        print("You can only take up to half of the remaining pieces left")
        playerTurn()
    if checkWinner():
        turn = 2
    else:
        turn = 1
        startGame()


def computerTurn():
    global totalPieces
    global turn

    print("It is the computer's turn!")
    print("There are " + str(totalPieces) + " pieces remaining")
    power = 0


    correctNum = False
    while not correctNum:
        if 2 ** power > int(totalPieces / 2):
            power -= 1
            correctNum = True
        else:
            power += 1

    if totalPieces != 2:
        takePieces = 2 ** power + 1
    else:
        takePieces = 1
    print("The computer took " + str(takePieces) + " marbles")
    totalPieces -= int(takePieces)
    if checkWinner():
        turn = 2
    else:
        turn = 0
        startGame()


def checkWinner():
    global totalPieces
    someoneWon = False
    if totalPieces == 1 and turn == 1:
        print("-----------------------------------------------------------------------------------------------------")
        print("You Lost!")
        someoneWon = True
    elif totalPieces == 1 and turn == 0:
        print("-----------------------------------------------------------------------------------------------------")
        print("You Won!")
        someoneWon = True
    return someoneWon


titleScreen()
