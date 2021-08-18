# Senses if one string is able to be rearranged into the other
def anagram(text1, text2):
    for char in text1:
        if char not in text2:
            return False
        elif text1.count(char) != text2.count(char):
            return False
    return True

text1 = input("Enter anagram: ")
text2 = input("Enter second anagram: ")

 # Ignore whitespace and capitals
noSpace1 = text1.lower().split()
noSpace1 = "".join(noSpace1)
noSpace2 = text2.lower().split()
noSpace2 = "".join(noSpace2)


if anagram(noSpace1, noSpace2):
    print("Anagram")
else:
    print("Not anagram")
