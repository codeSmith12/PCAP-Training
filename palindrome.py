def isPalindrome(text, begin, end):
    if begin == end:
        return True
    elif text[begin].lower() != text[end].lower():
        return False
    else:
        return isPalindrome(text, begin+1, end-1)


text = input("Enter text to check for palindrome: ")

noSpaces = text.split()
noSpaces = "".join(text)
if isPalindrome(noSpaces, 0, len(text)-1):
    print(text, "is a palindrome")
else:
    print(text, "is not a palindrome")
