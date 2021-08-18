import sys
from os import strerror

class StudentsDataException(Exception):
    pass


class BadLine(StudentsDataException):
    pass
    # Write your code here.


class FileEmpty(StudentsDataException):
    pass
    # Write your code here.

fileName = input("File name: ")

try:
    students = {}
    file = open(fileName, 'r')
    line = file.readline()
    if not line:
        raise FileEmpty
    else:
        while line != 0:
            entry = line.split()
            if not isinstance(entry[0], str) or not isinstance(entry[1], str) or not entry[2].isdigit():
                raise BadLine
            else:
                students["{} {}".format(entry[0], entry[1])] = int(entry[2])
                line = file.readline()

except BadLine:
    print("Bad line, format data better.")
    sys.exit()

except FileEmpty:
    print("File exists but is empty.")
    sys.exit()
except IOError as err:
    print("Error: ", strerror(err.errno))
    sys.exit()

for student in sorted(students):
    print("{} {}", student, students[student])
