# Git-hub repository:    https://github.com/IngoLitli/TileTraveller.git


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
    pull = input('Pull a lever (y/n): ').upper()
    if pull == 'Y':
        board[player[0]][player[1]][LEVER] = 0
        return 1
    return 0


"""[N,E,S,W, lever]"""
board = [
    [[0, 1, 1, 0, 0], [0, 1, 0, 1, 1], [0, 0, 1, 1, 0]],
    [[1, 1, 1, 0, 1], [0, 0, 1, 1, 1], [1, 0, 1, 0, 1]],
    [[1, 0, 0, 0, 0], [1, 0, 0, 0, 0], [1, 0, 0, 0, 0]]
    ]
inventory = 0

player = [2, 0]

printAvailableMoves(player)
LEVER = 4

while player != [2, 2]:
    direction = input("Direction: ").upper()
    if legalMove(player, direction):
        player = movePlayer(player, direction)
        inventory = hasCoin(inventory)
        if player != [2, 2]:
            printAvailableMoves(player)
    else:
        print("Not a valid direction!")
        printAvailableMoves(player)
else:
    print("Victory! Total coins {}.".format(inventory))
