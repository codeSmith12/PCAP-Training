import sys
if __name__ != "__main__":
    print("Run as main program, not as module.")
    sys.exit()
digits = input("Enter birthday in format: YYYYMMD or YYYYDDM or MMDDYYYY: ")
sum = 0
for digit in digits:
    sum += int(digit)
if sum >= 10:
    tmp = str(sum)
    sum = int(tmp[0]) + int(tmp[1])
print(sum)
