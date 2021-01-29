class Date:
    date = ""
    def __init__(self, n):
        self.date = n
    @classmethod
    def integer(cls,date):
        cls.date = date
        s = cls.date.split("-")
        if s[0][0] == 0:
            s[0].pop(0)
        if s[1][0] == 0:
            s[1].pop(0)
        cls.day = int(s[0])
        print("Day ",cls.day )
        cls.month = int(s[1])
        print("Month ", cls.month)
        cls.year = int(s[2])
        print("Year ", cls.year)
    @staticmethod
    def check(string):
        k=0
        s = string.split("-")
        day = int(s[0])
        month = int(s[1])
        year = int(s[2])
        if (month < 1 or month > 12):
            print("Wrong month")
            k=1
        if(day<1 or day > 31):
            print("Wrong day")
            k=1
        if((month==2) and day > 29):
            print("Wrong day")
            k=1
        if((month==4 or month ==6 or month==9 or month == 11)and day>30):
            print("Wrong day")
            k=1
        if(year<0):
            print("Wrong year")
            k=1
        if(not k):
            print("Right date")
date = input()
a = Date(date)
a.integer(date)
Date.check(date)




