"""
ID: Aryan Naveen
LANG: PYTHON2
TASK: ride
"""

def calculate(str):
    product = 1
    for char in str:
        product *= (ord(char)-64)

    return product % 47


fin = open("ride.in", 'r')
input = fin.read().splitlines()
fin.close()

comet = input[0]
group = input[1]

fout = open("ride.out", 'w')
output = ""
if(calculate(comet)==calculate(group)):
    output = "GO"
else:
    output = "STAY"

fout.write(output + "\n")
fout.close