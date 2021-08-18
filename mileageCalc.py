'''
TODO: Need to fix the ending mileage. It's carrying over from one camp to another
Somehow


'''





import sys
from os import system
if __name__ != "__main__":
    sys.exit()
class Camp:
    def __init__(self, str, subject, addr, dates, distance, daysHeld):
        self.str = str
        self.subject = subject
        self.addr = addr
        self.dates = dates
        self.distance = distance
        self.days = daysHeld
    def writeToString(self):
        self.str.append("|" + (self.subject + " " + self.dates).center(windowWidth-2)+"|")
        self.str.append("|" + " ".center(windowWidth-2)+"|")
        self.str.append("|" + ("Location: " + self.addr).center(windowWidth-2)+"|")
        self.str.append("|" + " ".center(windowWidth-2)+"|")
        self.str.append("|" + ("Distance From Home to Location: " + str(self.distance)).center(windowWidth-2)+"|")
        self.str.append("|" + " ".center(windowWidth-2)+"|")
        self.str.append("|" + ("Days Held: " + str(self.days)).center(windowWidth-2)+"|")
        self.str.append("|" + " ".center(windowWidth-2)+"|")
        self.str.append("|" + ("Total Week Mileage: " + str(self.distance*self.days*2)).center(windowWidth-2)+"|")
        self.str.append("-" * windowWidth) # Bar


weekDays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
milesCalc = {}
exit = False
name = input("What is your name? ")
homeAdr = input("What is your home address? ")
startingMileage = int(input("What was your starting mileage before any camps? "))
endingMileage = startingMileage
totalDistance = 0 # Total distance traveled throughout summer
numCamps = 0
windowWidth = 50
myStr = []
totalDistances = 0 # All home to location distances added up for averaging
camps = []




while not exit:
    numCamps += 1
    subject = input("What subject was the camp? ")
    campAdr = input("What is the camp address? ")
    dates = input("What were the dates(MM/DD - MM/DD)? ")
    distance = int(input("What is the distance in miles from home to camp? "))
    days = int(input("How many days did you work? "))
    camp = Camp(myStr, subject, campAdr, dates, distance, days)
    camps.append(camp)
    totalDistances += distance
    weeklyTotal = 0
    for i in range(days):
        weeklyTotal += distance * 2
        milesCalc[weekDays[i-1]] = endingMileage
    totalDistance += weeklyTotal
    endingMileage += weeklyTotal

    # After calculation, allows for multiple calculations
    exitProgram = input("Would you like to calculate another camp?(y/n only)")
    if exitProgram.lower() == 'y':
        milesCalc = {}
        pass
    else:
        exit = True

# Format the string to print

# General Stats
myStr.append("\n" + "-" * windowWidth) # Bar
myStr.append("|" + "2021 Summer Camp Mileage Report".center(windowWidth-2)+"|")
myStr.append("-" * windowWidth) # Bar
myStr.append("|" + name.center(windowWidth-2)+"|")
myStr.append("-" * windowWidth) # Bar
myStr.append("|" + "Summary".center(windowWidth-2)+"|")
myStr.append("|" + " ".center(windowWidth-2)+"|")
myStr.append("|" + ("Home Address: " + homeAdr).center(windowWidth-2)+"|")
myStr.append("|" + " ".center(windowWidth-2)+"|")
myStr.append("|" + ("Starting Milage: " + str(startingMileage)).center(windowWidth-2)+"|")
myStr.append("|" + " ".center(windowWidth-2)+"|")
myStr.append("|" + ("Ending Milage: " + str(endingMileage)).center(windowWidth-2)+"|")
myStr.append("|" + " ".center(windowWidth-2)+"|")
myStr.append("|" + ("Total Distance Traveled: " + str(totalDistance)).center(windowWidth-2)+"|")
myStr.append("|" + " ".center(windowWidth-2)+"|")
myStr.append("|" + ("Average Distance Traveled Per Camp: " + str("{:.2f}".format(totalDistance / numCamps))).center(windowWidth-2)+"|")
myStr.append("|" + " ".center(windowWidth-2)+"|")
myStr.append("|" + ("Average Distance From Home To Camp: " + str("{:.2f}".format(totalDistances / numCamps))).center(windowWidth-2)+"|")
myStr.append("|" + " ".center(windowWidth-2)+"|")
myStr.append("|" + ("Number of Camps: " + str(numCamps)).center(windowWidth-2)+"|")
myStr.append("-" * windowWidth) # Bar
myStr.append("|" + "Camps".center(windowWidth-2)+"|")
myStr.append("-" * windowWidth) # Bar

for camp in camps:
    camp.writeToString()


# Clear screen and print each line that was appended
system('cls')
for str in myStr:
    print(str)
