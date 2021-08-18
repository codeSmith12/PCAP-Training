from os import strerror

fileName = input("Enter name of file to open: ")
def checkAlpha(ch):
    return ch.isalpha()
try:
    file = open(fileName, 'r')
    data = file.read()
    file.close()


    # Scan through the data, adding each alpha into the dictionary with counts
    letterCounts = {}
    for ch in filter(checkAlpha,data.lower()):
        if ch not in letterCounts:
            letterCounts[ch] = 1
        else:
            letterCounts[ch] += 1

    sortedDict = dict(sorted(letterCounts.items(), key=lambda item: item[1], reverse=True))

    # Print the dictionary sorted by key...

    try:
        outputFile = open(fileName[:-4]+".hist",'w')
        for letter in sortedDict:
            print("{} -> {}".format(letter,sortedDict [letter]))
            outputFile.write("{} -> {}\n".format(letter,sortedDict [letter]))
        outputFile.close()
    except IOError as err:
        print("Error has occured: ", strerror(err.errno))

except IOError as err:
    print("Error has occured: ", strerror(err.errno))
