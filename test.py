"""
ID: Aryan Naveen
LANG: PYTHON2
TASK: test
"""

fin = open("test.in", 'r')
input = fin.read()
fin.close()

sum = int(input[:input.find(" ")]) + int(input[input.find(" ") + 1:])

output = open("test.out", 'w')
output.write(str(sum)+ "\n")
output.close()
