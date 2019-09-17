#Git-hub repository:    https://github.com/IngoLitli/TileTraveller.git

def printAvailableMoves(player):
    """Prints out all available moves for the player"""

def movePlayer(player, move):
    """Moves the player"""

    printAvailableMoves(player)
    return player

def legalMove(player, move):
    """Checks if the current direciton is a legal move"""

"""[N,S,E,W]"""
board = [
    [[0,1,1,0], [0,0,1,1], [0,1,0,1]],
    [[1,1,1,0], [0,1,0,1], [1,1,0,0]],
    [[1,0,0,0], [1,0,0,0], [1,0,0,0]]
    ]

player = [2,0]

printAvailableMoves(player)

while player != [2,2]:
    direction = input("Direction: ").upper()
    if legalMove(player, direction):
        player = movePlayer(player,direction)
else:
    print("Victory!")
