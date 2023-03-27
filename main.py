
def printBoard(board):
    for i in range(3):
        for j in range(3):
            print(board[i][j], end=" ")
        print()

def isDraw(board):
    for i in range(3):
        for j in range(3):
            if board[i][j] == '_':
                return False
    return True

def isWinner(board, player):
    for i in range(3):
        # Check rows
        if board[i][0] == player and board[i][1] == player and board[i][2] == player:
            return True
        # Check columns
        if board[0][i] == player and board[1][i] == player and board[2][i] == player:
            return True
    # Check diagonals
    if board[0][0] == player and board[1][1] == player and board[2][2] == player:
        return True
    if board[0][2] == player and board[1][1] == player and board[2][0] == player:
        return True
    return False


def playGame():
    board = [['_' for i in range(3)] for j in range(3)]
    player = 'X'
    while True:
        printBoard(board)
        row = int(input("Enter row for {} (0-2): ".format(player)))
        col = int(input("Enter column for {} (0-2): ".format(player)))
        if row>2 or col>2 or row<0 or col<0:
            print("Invalid Input. Try again.")
            continue
        if board[row][col] != '_':
            print("This spot is already filled. Try again.")
            continue
        board[row][col] = player
        if isWinner(board, player):
            printBoard(board)
            print("{} wins!".format(player))
            break
        if isDraw(board):
            printBoard(board)
            print("It's a draw!")
            break
        if player == 'X':
            player = 'O'
        else:
            player = 'X'


playGame()
