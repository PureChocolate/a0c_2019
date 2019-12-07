with open("in.txt", "r") as f:
    values = [str(n) for n in f.readlines()]
    for x in range(len(values)):
        values[x] = values[x].rstrip('\n').split(')')
    print values[:20]   
    obs = {}
    tot = {}
    obs['COM'] = None
    for x in values:
        if x[0] not in tot:
            tot[x[0]] = 1
        if x[1] not in tot:
            tot[x[1]] = 1
        if x[1] not in obs:
            obs[x[1]] = [x[0]]
        else:
            obs[x[0]].append(x[1])

val = []
for x in tot:
    if x[0] not in val:
        val.append(x)

def run(data):
    c = 0
    if obs[data] is None:
        return 0
    else:
        c += run(obs[data][0]) + 1
        return c
count = 0
for x in val:
    count += run(x)

print str(count) + " total direct/indect"

    
