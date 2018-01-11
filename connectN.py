import sys
sys.version

def displayBoard(board):
    # for i in range(len(board)):
    #     print(*board[temp[i]], sep=' ')
    print('\n'.join(' '.join(row) for row in board))

def placePiece(board, column, color):
    location = 0
    for i in range(len(temp)):
        if(temp[i] == 0):
            location += 1
    location -= 1

    if(color == "red"):
        board[column[location]] = "X"
    else:
        board[column[location]] = "O"

length = int(input("size of board: "))

#temp = []
#board = []
#for n in range(length):
#    temp.append(".")
#
#for i in range(length):
#    board.append(temp)

#board = [['.']*length]*length
board = [['.']*length for i in range(length)]

displayBoard(board)
placePiece(board, 3, "red")
