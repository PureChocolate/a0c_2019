with open("in.txt", "r") as f:
    values = [str(n) for n in f.readlines()]
    for x in range(len(values)):
        values[x] = values[x].rstrip('\n').split(')') 
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

# part 1 stuff
# val = []
# for x in tot:
#     if x[0] not in val:
#         val.append(x)]

stepsSan = []
stepsYou = []
def run(data,key,trigger):
    c = 0
    if trigger < 4:
        if obs[data] is key:
            return 0
        else:
            if trigger is 1: stepsYou.append(data)
            elif trigger is 0: stepsSan.append(data)
            c += run(obs[data][0],key,trigger) + 1
            return c
    else:
        if obs[data][0] in key: # is instead of in should have been fine but it didnt see key and data as equal???????
            return 0
        else:
            if trigger is 1: stepsYou.append(data)
            elif trigger is 0: stepsSan.append(data)
            c += run(obs[data][0],key,trigger) + 1
            return c
    

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
# count = 0]
# for x in val:
#     count += run(x)

# print str(count) + " total direct/indect"

    
