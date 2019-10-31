def overlap(interval, other):
    if(interval[0] > other[0]):
        return interval[0] <= other[1]
    else:
        return other[0] <= interval[1]


def maximize_interval(interval, other_intervals):
    start = interval[0]
    end = interval[1]
    diff = 0
    for other in other_intervals:
        difference = 0
        if(overlap(interval, other)):
            start = min(start, other[0])
            end = max(end, other[1])

        else:
            if(other[0] > interval[0])
                difference = other[0] - interval[1]
            else:
                difference = interval[0] - other[1]

            if(diff == 0):
                diff = difference
            elif(not difference == 0):
                diff = min(diff, difference)
            
    return (end - start), diff


#fin = open('milk2.in', 'r')
#input = fin.read().splitlines()[1:]
#fin.close()

input = 

intervals = []

for line in input:
    start = int(line[:line.find(" ")])
    finish = int(line[line.find(" ") + 1:])

    intervals.append([start, finish])

durations = []
differences = []

for interval in intervals:
    comp_intervals = intervals[].remove(interval)
    max_duration, difference = maximize_interval(interval, comp_intervals)

    durations.append(max_duration)
    differences.append(difference)

print(max(durations))
print(max(differences))
    
