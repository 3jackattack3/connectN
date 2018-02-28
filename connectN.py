import sys
sys.version

def displayBoard(board):
    # for i in range(len(board)):
    #     print(*board[temp[i]], sep=' ')
    print('\n'.join('  '.join(row) for row in board))
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
                winRed = checkSameDirection(board, board.index(column), j, "red", 1, 0)
                if(winRed == False):
                    winRed = checkSameDirection(board, board.index(column), j, "red", 0, -1)
                    if(winRed == False):
                        winRed = checkSameDirection(board, board.index(column), j, "red", 1, -1)
                        if(winRed == False):
                            winRed = checkSameDirection(board, board.index(column), j, "red", 1, 1)
            if column[j] == 'O':
                winBlack = checkSameDirection(board, board.index(column), j, "black", 1, 0)
                if winBlack == False:
                    winBlack = checkSameDirection(board, board.index(column), j, "black", 0, -1)
                    if winBlack == False:
                        winBlack = checkSameDirection(board, board.index(column), j, "black", 1, -1)
                        if winBlack == False:
                            winBlack = checkSameDirection(board, board.index(column), j, "black", 1, 1)
    return [winRed, winBlack]

def checkSameDirection(board, startx, starty, color, directionx, directiony):
    win = False
    if color == "red":
        counterRed = 1
    elif color == "black":
        counterBlack = 1

    if directionx == 1 and directiony == 0:  #checks horizontals
        for column in board:
            for index in range(starty, len(board)):
                if color == "red":
                    if column[index] == 'X':
                        counterRed += 1
                        counterBlack = 0
                elif color == "black":
                    if column[index] == 'O':
                        counterBlack += 1
                        counterRed = 0

    elif directionx == 0 and directiony == -1:  #checks verticals
        for index in range(len(board[startx])):
            if color == "red":
                if board[startx][index] == 'X':
                    counterRed += 1
                    counterBlack = 0
            elif color == "black":
                if board[startx][index] == 'O':
                    counterBlack += 1
                    counterRed = 0

    elif directionx == 1 and directiony == -1:  #checks down right diagonol, just a placeholder right now, need to change
        for column in board:
            for index in range(starty, len(board)):
                if color == "red":
                    if column[index] == 'X':
                        counterRed += 1
                        counterBlack = 0
                elif color == "black":
                    if column[index] == 'O':
                        counterBlack += 1
                        counterRed = 0

    elif directionx == 1 and directiony == 1:  #checks up right diagonal, just a placeholder right now, need to change
        for column in board:
            for index in range(starty, len(board)):
                if color == "red":
                    if column[index] == 'X':
                        counterRed += 1
                        counterBlack = 0
                elif color == "black":
                    if column[index] == 'O':
                        counterBlack += 1
                        counterRed = 0

    # for i in range(startx, len(board)):
    #     for j in range(starty, len(board[i])):
    #         if color == "red":
    #             counterRed += 1
    #         elif color == "black":
    #             counterBlack += 1

    if color == "red":
        if counterRed >= (len(board)+1)/2 + 1:
            win = True

    if color == "black":
        if counterBlack >= (len(board)+1)/2 + 1:
            win = True

    print("counterRed = ", counterRed, " and counterBlack = ", counterBlack)
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
board = [['.']*length for i in range(length-1)]

win = [False, False]

displayBoard(board)
placePiece(board, 3, "black")
placePiece(board, 3, "black")
# placePiece(board, 3, "red")
# placePiece(board, 3, "red")
# placePiece(board, 3, "red")
placePiece(board, 3, "red")
placePiece(board, 3, "red")

win = check(board)
displayBoard(board)
print(win)
