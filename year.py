year = int(input("Type a year: "))

if year % 4 == 0:
    print("przestępny")
else:
    print("ni chuj")


class LeapYear:
    def __init__(self, year):
        self.year = year

    def check_year(self):
        if self.year % 4 != 0:
            return False
        return True


chuj = LeapYear(2007)
print(chuj.check_year())
print("ALe małyski nienawidze")
