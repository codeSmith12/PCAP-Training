file = open("ipsum.txt", "r")
data = file.read()
print(data)
textList = data.split()
print(textList)
# Search each list item, and count every letters (lowercase forced) occurance
letterCounts = {}
letterCounts["Enigma"] = "Unsolvable Mystery."

for word in textList:
    for ch in word:
        if ch not in letterCounts:
            
            # Add ch to letterCounts, set value to 1
