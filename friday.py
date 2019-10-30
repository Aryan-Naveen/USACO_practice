"""
ID: Aryan Naveen
LANG: PYTHON2
TASK: friday
"""

class month():
    def __init__(self, startDay, length):
        self.startDay = startDay
        self.length = length
    
    def get_day_13th_occurs(self):
        return (self.startDay + 12) % 7

    def get_first_day_of_next_month(self):
        return (self.startDay + self.length) % 7

class year():
    def __init__(self, startDay, i):
        self.i = i
        self.startDay = startDay
        self.leapYear = (i%100 == 0 and (1900 + i) %400 == 0) or (not i%100 == 0 and i%4 == 0)
    
    def get_next_year_startDay(self):
        return self.start

    def get_thirteen_count(self):
        months_with_30_days = [3, 5, 8, 10]

        thirteen_count = [0, 0, 0, 0, 0, 0, 0]

        self.start = self.startDay
        
        for i in range(12):
            length = 0
            if(i in months_with_30_days):
                length = 30
            elif(i == 1):
                if(self.leapYear):
                    length = 29
                else:
                    length = 28
            else:
                length = 31
            
            Month = month(self.start, length)
            day = Month.get_day_13th_occurs()
            thirteen_count[day] += 1
            
            self.start = Month.get_first_day_of_next_month()

        return thirteen_count

fin = open("friday.in", 'r')
input = int(fin.read())
fin.close()

thirteen_count = [0, 0, 0, 0, 0, 0, 0]
start = 2
for i in range(input):
    yearObj = year(start, i)
    thirteen_count_year = yearObj.get_thirteen_count()
    for i in range(7):
        thirteen_count[i] += thirteen_count_year[i]
    start = yearObj.get_next_year_startDay()

fout = open("friday.out", 'w')
output = ""

for i in range(6):
    output += str(thirteen_count[i]) + " "

output += str(thirteen_count[6])

print(output)

fout.write(output + "\n")
