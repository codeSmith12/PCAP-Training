class WeekDayError(Exception):
    pass


class Weeker:
    def __init__(self, day):
        self.__days = ["Mon","Tue","Wed","Thu","Fri","Sat","Sun"]
        self.__day = ''
        if day not in self.__days:
            raise WeekDayError
        self.__day = day

    def __str__(self):
        return self.__day

    def add_days(self, n):
        index = self.__days.index(self.__day)
        index += n
        self.__day = self.__days[index%7]

    def subtract_days(self, n):
        index = self.__days.index(self.__day)
        index -= n
        self.__day = self.__days[index%7]


try:
    weekday = Weeker('Mon')
    print(weekday)
    weekday.add_days(15)
    print(weekday)
    weekday.subtract_days(23)
    print(weekday)
    weekday = Weeker('Monday')
except WeekDayError:
    print("Sorry, I can't serve your request.")
