from collections import defaultdict
with open("in.txt", "r") as f:
    lines = [str(x) for x in f.readlines()]
    a = lines[0].split(',')
    b = lines[1].split(',')
    data = []
    data.append(a)
    data.append(b)
    direc = {'R': (1, 0), 'D': (0,-1),'U': (0,1), 'L': (-1,0)} 

    intersection = []
    been = defaultdict(dict)    
    part2 = True
    
    for i in range(len(data)):
        tSteps = 0
        cord = (0,0)
        line = data[i]
        for step in line:
            move = step[0]
            num = int(step[1:])
            for n in range(num):
                tSteps += 1
                cord = tuple(cord[k] + direc[move][k] for k in range(len(cord)))
                if cord not in been:
                    been[cord] = (i,tSteps)
                else:
                    if been[cord][0] is not i:
                        tup3 = tSteps,been[cord][1]
                        if part2 is True: intersection.append(tup3)
                        else: intersection.append(cord)
    small = int
    #part 1
    # for x in intersection:
    #     if( (abs(0 - x[0]) + abs(0 - x[1])) < small): small = (abs(0 - x[0]) + abs(0 - x[1]))

    # part 2
    for x in intersection:
        if x[0] + x[1] < small: small = x[0] + x[1]    
    print small