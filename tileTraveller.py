#Git-hub repository:    https://github.com/IngoLitli/TileTraveller.git

def printAvailableMoves(player):
    """Prints out all available moves for the player"""
    
    moves = ["(N)orth","(S)outh","(E)ast","(W)est"]
    availables = []
    for i in range (4):
        if board[player[0]][player[1]][i]:
            availables.append(moves[i])
    
    print("You can travel:", end=" ")
    print(" or ".join(availables)+".")

def movePlayer(player, move):
    """Moves the player"""

    printAvailableMoves(player)
    return player

def playerPosition():
    """Returns the playerpostion on board"""
    return (board[player[0]][player[1]])

def legalMove(player, move):
    """Checks if the current direciton is a legal move"""
    if move == "N" and playerPosition()[0]:
        return True
    elif move == "S" and playerPosition()[1]:
        return True
    elif move == "E" and playerPosition()[2]:
        return True
    elif move == "W" and playerPosition()[3]:
        return True
    return False

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
        print("Not a valid direction!")
else:
    print("Victory!")
