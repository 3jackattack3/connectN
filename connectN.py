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
        if board[i][column] == '.':
            location += 1
    location -= 1

    if color == "red":
        board[location][column] = 'X'
    else:
        board[location][column]= 'O'

# def checkVerticals(board):
#     counter = 0
#     winRed = False
#     winBlack = False
#     for column in range(len(board)):
#         for i in range(int((len(board)-1)/2)):
#             for j in range(int((len(board)+1)/2)):
#                 if(board[j][column] == board[j+1][column]):
#                     counter += 1
#                 if(counter >= (len(board)+1)/2 and board[j][column] == 'X'):
#                     winRed = True
#                 if(counter >= (len(board)+1)/2 and board[j][column] == 'O'):
#                     winBlack = True
#                 counter = 0
#     return [winRed, winBlack]

def check(board):
    winRed = False
    winBlack = False
    for column in board:
        for j in range(len(board)):
            if column[j] == 'X':
                winRed = checkSameDirection(board, board.index(column), j, "red")
            if column[j] == 'O':
                winBlack = checkSameDirection(board, board.index(column), j, "black")
    return [winRed, winBlack]

def checkSameDirection(board, startx, starty, color):
    print("in function")
    win = False
    if color == "red":
        counterRed = 1
    elif color == "black":
        counterBlack = 1

    for i in range(startx, len(board)):
        for j in range(starty, len(board[column])):
            if color == "red":
                counterRed += 1
            elif color == "black":
                counterBlack += 1

    if counterRed >= (len(board)+1)/2 or counterBlack >= (len(board)+1)/2:
        win = True

    return win


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
win = check(board)
displayBoard(board)
print(win)
