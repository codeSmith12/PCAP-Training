# PROPER WAY OF OPENING FILES
from os import strerror

try:
    for line in open("LunaReceipt.txt", 'r'):
        print(line)
    # Actual processing goes here.
except Exception as exc:
    print("The file could not be opened:", strerror(exc.errno))
