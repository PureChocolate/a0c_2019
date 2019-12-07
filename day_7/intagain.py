from collections import Counter
with open("in.txt", "r") as f:
    values = [int(n) for n in f.read().split(',')]

test = [3,15,3,16,1002,16,10,16,1,16,15,15,4,15,99,0,0]

def run(nums, ins,ins2):
    count = 0
    i = 0
    while True:
        pNum = [int(x) for x in str(nums[i])]
        sNum = (0 if len(pNum) == 1 else pNum[-2])*10 + pNum[-1]
        pNum = pNum[:-2]
        if sNum == 1:
            while len(pNum) < 3:
                pNum = [0] + pNum
            st1, st2, st3 = nums[i+1], nums[i+2], nums[i+3]
            p1 = st1 if pNum[2] == 1 else nums[st1]
            p2 = st2 if pNum[1] == 1 else nums[st2]
            nums[st3] = p1 + p2
            i += 4
        elif sNum == 2:
            while len(pNum) < 3:
                pNum = [0] + pNum
            st1, st2, st3 = nums[i+1], nums[i+2], nums[i+3]
            p1 = st1 if pNum[2] == 1 else nums[st1]
            p2 = st2 if pNum[1] == 1 else nums[st2]
            nums[st3] = p1 * p2
            i += 4
        elif sNum == 3:
            if count == 0:
                nums[nums[i+1]] = ins
                count = 1
            else:
                nums[nums[i+1]] = ins2
            i += 2
        elif sNum == 4:
            #print(str(nums[nums[i + 1]]) + " printed with opcode 4")
            return nums[nums[i + 1]]
            i += 2
        elif sNum == 5 or sNum == 6:
            while len(pNum) < 3:
                pNum = [0] + pNum
            st1, st2 = nums[i+1], nums[i+2]
            p1 = st1 if pNum[2] == 1 else nums[st1]
            p2 = st2 if pNum[1] == 1 else nums[st2]
            if sNum == 5:
                if p1 != 0: 
                    i = p2
                else: i += 3
            elif sNum == 6:
                if p1 == 0:
                    i = p2
                else:
                    i += 3
        elif sNum == 7 or sNum == 8:
            while len(pNum) < 3:
                pNum = [0] + pNum
            st1, st2, st3 = nums[i+1], nums[i+2], nums[i+3]
            p1 = st1 if pNum[2] == 1 else nums[st1]
            p2 = st2 if pNum[1] == 1 else nums[st2]
            if sNum is 7: nums[st3] = 1 if p1 < p2 else 0
            elif sNum is 8: nums[st3] = 1 if p1 == p2 else 0
            i += 4
        else:
            assert sNum is 99
            break

def d7run(test,s):
    a = run(test,s[0],0)
    b = run(test,s[1],a)
    c = run(test,s[2],b)
    d = run(test,s[3],c)
    e = run(test,s[4],d)
    print e

def dub(temp):
    tc = Counter(str(temp))
    for x in tc:
        if tc[x] is 2:
            return True

def progress(comb,c,n):
    comb[c] = comb[c] + 1 if n is 1 else comb[c]
    newComb = []
    for x in comb:
        if x is comb[c]:            
            newComb.append(x)
            print "hit"
        else:
            if x + 1 > 5:
                x = x + 1
            else:
                print "bruh"
            newComb.append(x)
            # print x
    return newComb

inc = 0
track = 0
seq = [0,1,2,3,4]
mthrust = []
i = 0
while i < 20:
    print seq
    mthrust.append(d7run(values, seq))
    progress(seq,track, inc)
    i += 1
    inSeq = sum(d * 10**i for i, d in enumerate(seq[::-1]))
    # print inSeq
    if dub(inSeq) is False:
        print "wtf"
    if i % 20 is 0:
        track += 1
    if i % 4 is 0: inc = 1
    else: inc = 0