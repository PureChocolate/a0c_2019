from collections import defaultdict
with open("in.txt", "r") as f:
    lines = [str(x) for x in f.readlines()]
    a = lines[0].split(',')
    b = lines[1].split(',')
    data = []
    data.append(a)
    data.append(b)

    intersection = []
    been = defaultdict(dict)
    
    direc = {'R': (1, 0), 'D': (0,-1),'U': (0,1), 'L': (-1,0)}

    for i in range(len(data)):
        cord = (0,0)
        line = data[i]
        for step in line:
            move = step[0]
            num = int(step[1:])
            for n in range(num):
                cord = tuple(cord[k] + direc[move][k] for k in range(len(cord)))
                if cord not in been:
                    been[cord] = i
                else:
                    if been[cord] is not i: intersection.append(cord)
    small = int
    for x in intersection:
        if( (abs(0 - x[0]) + abs(0 - x[1])) < small): small = (abs(0 - x[0]) + abs(0 - x[1]))        
    print small