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
        while len(line) != 0:
            entry = line.split()
            print(entry)
            entry[2] = float(entry[2])
            print(entry[2])
            if not isinstance(entry[0], str) or not isinstance(entry[1], str):
                raise BadLine
            else:
                if "{} {}".format(entry[0], entry[1]) in students:
                    students["{} {}".format(entry[0], entry[1])] += entry[2]
                else:
                    students["{} {}".format(entry[0], entry[1])] = entry[2]
                line = file.readline()
        file.close()
except BadLine:
    print("Bad line, format data better.")
    sys.exit()

except FileEmpty:
    print("File exists but is empty.")
    sys.exit()
except IOError as err:
    print("Error: ", strerror(err.errno))
    sys.exit()
finally:
    for student in sorted(students):
        print("{} {}".format( student, students[student]))
