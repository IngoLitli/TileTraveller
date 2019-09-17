#Git-hub repository:    https://github.com/IngoLitli/TileTraveller.git

def printAvailableMoves(player):
    """Prints out all available moves for the player"""
    
    moves = ["(N)orth","(E)ast","(S)outh","(W)est"]
    availables = []
    for i in range (4):
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

    if player != [2,2]:
        printAvailableMoves(player)
    return player

def playerPosition():
    """Returns the playerpostion on board"""
    return (board[player[0]][player[1]])

def legalMove(player, move):
    """Checks if the current direciton is a legal move"""
    Moves = ["N","E","S","W"]
    if playerPosition()[Moves.index(move)]:
        return True
    return False

"""[N,S,E,W]"""
board = [
    [[0,1,1,0], [0,1,0,1], [0,0,1,1]],
    [[1,1,1,0], [0,0,1,1], [1,0,1,0]],
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
