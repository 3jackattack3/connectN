import sys
sys.version

def displayBoard(board):
    # for i in range(len(board)):
    #     print(*board[temp[i]], sep=' ')
    print('\n'.join(' '.join(row) for row in board))
    print('\n')

def placePiece(board, column, color):
    location = 0
    for i in range(len(board)):
        if(board[i][column] == '.'):
            location += 1
    location -= 1

    if(color == "red"):
        board[location][column] = 'X'
    else:
        board[location][column]= 'O'

def checkVerticals(board):
    counter = 0
    winRed = False
    winBlack = False
    for column in range(len(board)):
        for i in range(int((len(board)-1)/2)):
            for j in range(int((len(board)+1)/2)):
                if(board[j][column] == board[j+1][column]):
                    counter += 1
                if(counter >= (len(board)+1)/2 and board[j][column] == 'X'):
                    winRed = True
                if(counter >= (len(board)+1)/2 and board[j][column] == 'O'):
                    winBlack = True
                counter = 0
    return [winRed, winBlack]

def check(board, counterRed, counterBlack, startx, starty):
    for i in range(startx, len(board)):
        for j in range(starty, len(board[column])):
            if(board[j][column] == 'X'):
                #check(board, counterRed+1, counterBlack)
            #if


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

win = [False, False]

displayBoard(board)
placePiece(board, 3, "red")
placePiece(board, 3, "red")
placePiece(board, 3, "red")
placePiece(board, 3, "red")
placePiece(board, 3, "red")
win = checkVerticals(board)
displayBoard(board)
print(win)
