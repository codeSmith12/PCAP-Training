nums = input("Enter numbers: ")

digits = []

def convertDigit(num):
    digit = [[' ',' ',' '],[' ',' ',' '],[' ',' ',' '],[' ',' ',' '],[' ',' ' ,' ']]
    if num== "1":
        digit[0][2] = '#'
        digit[1][2] = '#'
        digit[2][2] = '#'
        digit[3][2] = '#'
        digit[4][2] = '#'
    elif num == "2":

        digit[0][0] = '#'
        digit[0][1] = '#'
        digit[0][2] = '#'

        digit[1][2] = '#'

        digit[2][0] = '#'
        digit[2][1] = '#'
        digit[2][2] = '#'

        digit[3][0] = '#'

        digit[4][0] = '#'
        digit[4][1] = '#'
        digit[4][2] = '#'

    elif num == "3":

        digit[0][0] = '#'
        digit[0][1] = '#'
        digit[0][2] = '#'

        digit[1][2] = '#'

        digit[2][0] = '#'
        digit[2][1] = '#'
        digit[2][2] = '#'

        digit[3][2] = '#'

        digit[4][0] = '#'
        digit[4][1] = '#'
        digit[4][2] = '#'

    elif num== "4":

        digit[0][0] = '#'
        digit[0][2] = '#'

        digit[1][2] = '#'
        digit[1][0] = '#'

        digit[2][0] = '#'
        digit[2][1] = '#'
        digit[2][2] = '#'

        digit[3][2] = '#'

        digit[4][2] = '#'

    elif num== "5":

        digit[0][0] = '#'
        digit[0][1] = '#'
        digit[0][2] = '#'

        digit[1][0] = '#'

        digit[2][0] = '#'
        digit[2][1] = '#'
        digit[2][2] = '#'

        digit[3][2] = '#'

        digit[4][0] = '#'
        digit[4][1] = '#'
        digit[4][2] = '#'

    elif num == "6":

        digit[0][0] = '#'
        digit[0][1] = '#'
        digit[0][2] = '#'

        digit[1][0] = '#'

        digit[2][0] = '#'
        digit[2][1] = '#'
        digit[2][2] = '#'

        digit[3][0] = '#'
        digit[3][2] = '#'

        digit[4][0] = '#'
        digit[4][1] = '#'
        digit[4][2] = '#'

    elif num== "7":
        digit[0][0] = '#'
        digit[0][1] = '#'
        digit[0][2] = '#'
        digit[1][2] = '#'
        digit[2][2] = '#'
        digit[3][2] = '#'
        digit[4][2] = '#'

    elif num == "8":

        digit[0][0] = '#'
        digit[0][1] = '#'
        digit[0][2] = '#'

        digit[1][0] = '#'
        digit[1][2] = '#'

        digit[2][0] = '#'
        digit[2][1] = '#'
        digit[2][2] = '#'

        digit[3][0] = '#'
        digit[3][2] = '#'

        digit[4][0] = '#'
        digit[4][1] = '#'
        digit[4][2] = '#'

    elif num == "9":

        digit[0][0] = '#'
        digit[0][1] = '#'
        digit[0][2] = '#'

        digit[1][0] = '#'
        digit[1][2] = '#'

        digit[2][0] = '#'
        digit[2][1] = '#'
        digit[2][2] = '#'

        digit[3][2] = '#'

        digit[4][0] = '#'
        digit[4][1] = '#'
        digit[4][2] = '#'

    elif num == "0":

        digit[0][0] = '#'
        digit[0][1] = '#'
        digit[0][2] = '#'

        digit[1][0] = '#'
        digit[1][2] = '#'

        digit[2][0] = '#'
        digit[2][2] = '#'

        digit[3][2] = '#'
        digit[3][0] = '#'

        digit[4][0] = '#'
        digit[4][1] = '#'
        digit[4][2] = '#'

    return digit

def displayDigit(digit):
    for i in range(5):
        for j in range(3):
            print(digit[i][j], end='')
        print(" \n")

def displayDigits(digits):
    for curRow in range(5): # Iterate through each row
        for digit in digits: # For every digit we have, go through each column
            for i in range(3):
                print(digit[curRow][i], end='')
            print(" ", end='') # Space between each number
        print("\n") # Start new row

for num in nums:
    digits.append(convertDigit(num))

displayDigits(digits)
