with open("in.txt", "r") as f:
    values = [int(n) for n in f.read().split(',')]

# print len(values)

test = [3,225,1,225,6,6,1100]

def run(nums):
    i = 0
    while True:
        sNum = str(nums[i])[-2:]
        pNum = str(nums[i])[:-2]
        if len(pNum) < 2: pNum = ("0" * (2 - len(pNum))) + pNum
        if '1' in sNum:
            st1, st2, st3 = nums[i+1], nums[i+2], nums[i+3]
            p1 = 0
            p2 = 0
            p1 = st1 if pNum[1] is '1' else nums[st1]
            p2 = st2 if pNum[0] is '1' else nums[st2]
            nums[st3] = p1 + p2
            i += 4
        elif '2' in sNum:
            st1, st2, st3 = nums[i+1], nums[i+2], nums[i+3]
            p1 = 0
            p2 = 0
            p1 = st1 if pNum[1] is '1' else nums[st1]
            p2 = st2 if pNum[0] is '1' else nums[st2]
            nums[st3] = p1 * p2
            i += 4
        elif '3' in sNum:
            nums[nums[i+1]] = 1
            i += 2
        elif '4' in sNum: 
            print str(nums[i + 1]) + "printed"
            i += 2
        elif '99' in sNum:
            exit()
        else:
            print "something went wrong" + str(nums[i])
            i += 1
    #if nums[0] == 19690720: print(100 * nums[1] + nums[2])

run(values)
# temp = str(1002)[:-2]
# if len(temp) < 2: temp = ("0" * (2 - len(temp))) + temp
# # temp = temp[:-2]
# print temp[0]

# for n1 in range(100):
#     for n2 in range(100):
#         num1 = values[:] # or use values[:], god damn wasted majority of the 1.5 hours on this 
#         num1[1] = n1
#         num1[2] = n2
#         run(num1)