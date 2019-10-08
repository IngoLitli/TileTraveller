# Git-hub repository:    https://github.com/IngoLitli/TileTraveller.git
import random
LEVER = 4
DIRECTIONS = 'n','e','s','w'
LEVER_CHOICE = 'y','n'
def printAvailableMoves(player):
    """Prints out all available moves for the player"""

    moves = ["(N)orth", "(E)ast", "(S)outh", "(W)est"]
    availables = []
    for i in range(4):
        if board[player[0]][player[1]][i]:
            availables.append(moves[i])

    print("You can travel:", end=" ")
    print(" or ".join(availables)+".")


def movePlayer(player, move):
    """Moves the player"""
    if move == "N":
        player[0] -= 1
    elif move == "S":
        player[0] += 1
    if move == "E":
        player[1] += 1
    elif move == "W":
        player[1] -= 1

    return player


def playerPosition():
    """Returns the playerpostion on board"""
    return (board[player[0]][player[1]])


def legalMove(player, move):
    """Checks if the current direciton is a legal move"""
    Moves = ["N", "E", "S", "W"]
    if playerPosition()[Moves.index(move)]:
        return True
    return False


def hasCoin(inventory):
    if playerPosition()[LEVER]:
        pulled = pullLever()
        if pulled:
            inventory += pulled
            print('You received 1 coin, your total is now {}.'.format(inventory))
    return inventory


def pullLever():
    pull = random.choice(LEVER_CHOICE)
    # input('Pull a lever (y/n): ').upper()
    print('Pull a lever (y/n):',pull)
    if pull == 'y':
        return 1
    return 0


def play():
    if input("Play again (y/n): ").upper() == "Y":
        return True
    return False

"""[N,E,S,W, lever]"""
board = [
    [[0, 1, 1, 0, 0], [0, 1, 0, 1, 1], [0, 0, 1, 1, 0]],
    [[1, 1, 1, 0, 1], [0, 0, 1, 1, 1], [1, 0, 1, 0, 1]],
    [[1, 0, 0, 0, 0], [1, 0, 0, 0, 0], [1, 0, 0, 0, 0]]
    ]

random.seed(int(input('Input seed: ')))


run = True
while run:
    inventory = 0
    player = [2, 0]
    valid_moves = 0
    printAvailableMoves(player)


    while player != [2, 2]:
        #direction = input("Direction: ").upper()
        direction = random.choice(DIRECTIONS).upper()
        print('Direction:', direction.lower())
        if legalMove(player, direction):
            valid_moves +=1
            player = movePlayer(player, direction)
            inventory = hasCoin(inventory)
            if player != [2, 2]:
                printAvailableMoves(player)
        else:
            print("Not a valid direction!")
            printAvailableMoves(player)
    else:
        print("Victory! Total coins {}. Valid moves {}.".format(inventory,valid_moves))
        run = play()
