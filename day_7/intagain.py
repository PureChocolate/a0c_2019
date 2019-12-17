from itertools import permutations
with open("in.txt", "r") as f:
    nums = [int(n) for n in f.read().split(',')]

# nums = [3,26,1001,26,-4,26,3,27,1002,27,2,27,1,27,26,27,4,27,1001,28,-1,28,1005,28,6,99,0,0,5] #[3,15,3,16,1002,16,10,16,1,16,15,15,4,15,99,0,0]

def run(inputs,i=0):
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
        elif sNum is 3:
            nums[nums[i+1]] = inputs.pop(0)
            i1 = nums[i+1]
            i += 2
        elif sNum is 4: 
            return nums[nums[i+1]], i + 2
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
            return 99,i


# ty god llyr for this code :bow2
def runTrue(a, b):
    max = 0
    for perm in permutations(range(a, b)): # go through all combos?
        oldVal = 0 
        i = [0,0,0,0,0] # initial index for each amp?
        values = i[:]# copy the indexes list?
        seq = [[perm[c]] for c in range(len(perm))] #get each phase setting and store as a list(stack?) ??
        seq[0].append(0) # add the initial 0 input for amp A /add a 0 at the front of the list/stack??
        stop = False
        while not stop: # continue till end
            for j in range(len(perm)):# for every phase code/amp
                # run the intcode computer and get the return value and index where it stoped
                # run by giving the phase setting (initially since they are poped out of the list by the time -
                # the amp has to run the 2nd time so its just the output value from last amp)
                #also give the index from where it left off (initially all are 0s as initialized above)
                oldVal, i[j] = run(seq[j], i[j])
                seq[(j+1) % len(seq)].append(oldVal) #????????????
                # + 1 to access the next element as first is empty (?) and
                # mod 5 to make sure you dont go out of bounds(?)
                if oldVal == 99: # end code/value
                    if values[-1] > max: 
                        # if last value outputed by the program (since we hit stop code) 
                        # is bigger than current max
                        max = values[-1] # change it
                    stop = True # break and go to next combination
                    break
                else: #else continue and add the output from the amps to the index of the respective amp
                    values[j] = oldVal
    return max

print runTrue(5,10)

# CAN JUST USE PERMUTATIONS INSTEAD OF MANUALY GOING THROUGH
# def progress(comb,c,n):
#     temp = comb[c]
#     if n is 1:
#         comb[0],comb[1],comb[2],comb[3],comb[4] = 5,6,7,8,9
#         comb[c] = temp + 1
#     for x in range(len(comb)):
#         if comb[x] == comb[c] and x != c:
#             comb[x] = 35 - ((comb[0] + comb[1] + comb[2] + comb[3] + comb[4]) - comb[x])
#     for x in range(len(comb)):
#         if comb[x] is comb[c]:
#             comb[x] = comb[x]
#         else:
#             try:
#                 temp2 = comb[x + 1]
#                 comb[x+1] = comb[x]
#                 comb[x] = temp2
#             except:
#                 continue
    
#     for i in range(len(comb)):
#         if comb[i] == 10:
#             comb[i] = 35- ((comb[0] + comb[1] + comb[2] + comb[3] + comb[4]) - comb[i])

#     return comb
# inc = 0
# track = 0

# mthrust = []
# i = 0   
# while i < 120:
#     # print seq
#     mthrust.append(d7run(values, seq,True))
#     progress(seq,track, inc)
#     i += 1
#     if i % 20 is 0:
#         track += 1
#     if i % 4 is 0: inc = 1
#     else: inc = 0

# print mthrust
# d7run(test)
# max = 0
# for x in mthrust:
#     if x > max : max = x
# print str(max) + "max"