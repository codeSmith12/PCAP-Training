import sys
# Turn into a gui project???
'''Python Institude Sudoku Challenge '''

if __name__ != "__main__":
    print("Run as main program, not as module.")
    sys.exit()

def createBoard():
    board = []
    curRow = []
    for i in range(9):
        rowValues = input("Enter a row of numbers for the sudoku board: ")
        for val in rowValues:
            curRow.append(int(val))
        board.append(curRow)
        curRow = []
    return board
def displayBoard(board):
    for row in board:
        for col in row:
            print(col, end=" ")
        print("\n")
def checkRows(board):
    for row in range(9):
        if 1 not in board[row]:
            return False
        elif 2 not in board[row]:
            return False
        elif 3 not in board[row]:
            return False
        elif 4 not in board[row]:
            return False
        elif 5 not in board[row]:
            return False
        elif 6 not in board[row]:
            return False
        elif 7 not in board[row]:
            return False
        elif 8 not in board[row]:
            return False
        elif 9 not in board[row]:
            return False
    return True
def checkCols(board):
    for col in range(9):
        curCol = []
        for row in range(9):
            curCol.append(board[row][col])
        if 1 not in curCol:
            return False
        elif 2 not in curCol:
            return False
        elif 3 not in curCol:
            return False
        elif 4 not in curCol:
            return False
        elif 5 not in curCol:
            return False
        elif 6 not in curCol:
            return False
        elif 7 not in curCol:
            return False
        elif 8 not in curCol:
            return False
        elif 9 not in curCol:
            return False
    return True

for i in range(0,6,3):
    print(i)


def check3x3s(board):
    for curRow in range(0,9,3):
        for curCol in range(0, 9, 3):
            myStr=[]
            myStr += board[curRow][curCol:curCol+3]
            myStr += board[curRow+1][curCol:curCol+3]
            myStr += board[curRow+2][curCol:curCol+3]
            if 1 not in myStr:
                return False
            elif 2 not in myStr:
                return False
            elif 3 not in myStr:
                return False
            elif 4 not in myStr:
                return False
            elif 5 not in myStr:
                return False
            elif 6 not in myStr:
                return False
            elif 7 not in myStr:
                return False
            elif 8 not in myStr:
                return False
            elif 9 not in myStr:
                return False
    return True


def checkWin(board):
    if not checkCols(board):
        return False
    elif not checkRows(board):
        return False
    elif not check3x3s(board):
        return False
    else:
        return True


board = createBoard()
displayBoard(board)
if checkWin(board):
    print("Values are valid, winner!")
else:
    print("Values are not valid, loser :(")
