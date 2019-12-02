import math;
total = 0

def fuelReq(m):
    global total
    if((math.floor(m/3) - 2) < 0):
        total += 0
    else:
        m = int((math.floor(m/3)) - 2)
        total += m
        fuelReq(m)

with open("masses.txt") as f:
    for line in f:
        line = int(line)
        fuelReq(line)

print total