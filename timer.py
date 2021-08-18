class Timer:
    def __init__(self, hrs=0, mins=0, secs=0):
        self.hrs = hrs
        self.mins = mins
        self.secs = secs

    def __str__(self):
        myStr = "{:d}:".format(self.hrs)
        myStr += "{:d}:".format(self.mins)
        myStr += "{:d}".format(self.secs)
        return "".join(myStr)

    def next_second(self):
        self.secs += 1
        if self.secs == 60:
            self.secs = 0
            self.mins += 1
        if self.mins == 60:
            self.mins = 0
            self.hrs += 1
        if self.hrs == 24:
            self.hrs = 0
            self.mins = 0
            self.secs = 0


    def prev_second(self):
        self.secs -= 1
        if self.secs <= 0:
            self.secs = 59
            self.mins -= 1
        if self.mins <= 0:
            self.mins = 59
            self.hrs -= 1
        if self.hrs <= 0:
            self.hrs = 23


timer = Timer(23, 59, 59)
print(timer)
timer.next_second()
print(timer)
timer.prev_second()
print(timer)
