"""
ID: Aryan Naveen
LANG: PYTHON2
TASK: 
"""

testing = False
num_test_files = 0
task_name = ""

def task(input):
    #Write code for task in here

def verify(output, i):
    file = 'data/' + task_name + '/' + str(i + 1) + '.out'
    solution = file.read().splitlines()
    file.close()
    return output == solution

if(testing):
    count = 0
    for i in range(num_test_files):
        file = 'data/' + task_name + '/' + str(i + 1) + '.in'
        fin = open(file, 'r')
        input = fin.read().splitlines()
        output = task(input)
        if(verify(output, i)):
            count += 1
        else:
            print('File Number:' + str(i + 1))
            print('Your output:' + str(output))
    print("The percentage of correct answers was " + str((count/num_test_files)*100) + "%")

else:
    file = task_name + ".in"
    fin = open(file, 'r')
    output = task(fin.read().splitlines())
    fin.close()

    fout = task_name + '.out'
    fout.write(output + '\n')
    fout.close()
