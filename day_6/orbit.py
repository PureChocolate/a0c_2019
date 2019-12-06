with open("in.txt", "r") as f:
    values = [str(n) for n in f.readlines()]
    for x in range(len(values)):
        values[x] = values[x][:-1].split(')')
    obs = {}
    for x in values:
        if x[0] not in obs:
            obs[x[0]] = [x[1]]
        else:
            obs[x[0]].append(x[1])\
print obs
    
