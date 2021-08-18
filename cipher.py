if __name__ == "__main__":
    print("Good job")
else:
    sys.exit()

import sys

def encrypt(text, key):
    message = ""
    print("Encrypting message \'" + text + "\' with key", key, "\n")
    for char in text:
        if char.islower():
            newChar = ord(char) # z = 122 + 1 - 97 = 26%26 = 0 + 97 = 'a'
            newChar = chr((newChar  + key - ord('a')) % 26 + ord('a'))
            message += newChar
        elif char.isupper():
            newChar = ord(char) # z = 122 + 1 - 97 = 26%26 = 0 + 97 = 'a'
            newChar = chr((newChar  + key - ord('A')) % 26 + ord('A'))
            message += newChar
        else:
            message += char
    return message

key = 0
text = ""
text = input("Enter message to be encrypted: ")
while key < 1 or  key > 25:
    key = int(input("Enter key number (1-25): "))

print(encrypt(text, key))
