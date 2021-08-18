import sys
if __name__ != "__main__":
    print("Run as main program, not as module.")
    sys.exit()

def hiddenString(str1, str2):
    lastChar = -1
    for char in str1:
        index = str2.find(char)
        if index < 0:
            return False
        elif index < lastChar:
            return False
        else:
            lastChar = index 

    return True

str1 = input("Enter string1: ").lower()
str2 = input("Enter string2: ").lower()
# Find returns -1 when it cant find the letter
if hiddenString(str1, str2):
    print("Yes")
else:
    print("No")
