with open("in.txt", "r") as f:
    values = [str(n) for n in f.readlines()]
    for x in range(len(values)):
        values[x] = values[x].rstrip('\n').split(')') 
    obs = {}
    tot = {}
    obs['COM'] = None
    for x in values:
        if x[0] not in tot or x[1] not in tot:
            tot[x[0]] = 1
            tot[x[1]] = 1
        if x[1] not in obs: obs[x[1]] = [x[0]]
        else: obs[x[0]].append(x[1])

# part 1 stuff
val = []
for x in tot:
    if x[0] not in val:
        val.append(x)

stepsSan = []
stepsYou = []
def run(data,key,trigger):
    c = 0
    if obs[data] is key or key in obs[data]:
        return 0
    else:
        if trigger is 1: stepsYou.append(data)
        elif trigger is 0: stepsSan.append(data)
        c += run(obs[data][0],key,trigger) + 1
        return c
        
#part 2
run('YOU',None,1)
run('SAN',None,0)
comKey = ''
for i in stepsSan:
    if i in stepsYou:
        comKey = i
        break

runYou = run('YOU',comKey,4)
runSan = run('SAN',comKey,4)
print runYou + runSan

# part 1
# count = 0
# for x in val:
#     count += run(x,None,3)
# print str(count) + " total direct/indect"