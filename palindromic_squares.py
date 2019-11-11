"""
ID: Aryan Naveen
LANG: PYTHON2
TASK: palsquare
"""

def add_value(num):
    if(num >= 0 and num <= 9):
        return chr(num + ord('0'))
    else:
        return chr(num + ord('A'))

def convert_to_base_B(decimal, base):
    conv = ""
    while(decimal > 0):
        conv += add_value(decimal % base)
        decimal = int(decimal/base)

    return conv[::-1], conv

def palindrome_check(decimal, base):
    baseB, baseBinverted = convert_to_base_B(decimal, base)

    return baseB == baseBinverted




def solve(base):
    output = ""
    
    for i in range(301):
        square = i ** 2

        i_in_B, _ = convert_to_base_B(i, base)
        square_in_B, _ = convert_to_base_B(square, base)
        
        if(palindrome_check(square, base)):
            output += i_in_B + " " + square_in_B + "\n"

    return output

fin = open('palsquare.in', 'r')
input = int(fin.read().splitlines()[0])
fin.close()

fout = open('palsquare.out', 'w')
fout.write(solve(input))
fout.close()
