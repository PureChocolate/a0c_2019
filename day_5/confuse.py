with open("in.txt", "r") as f:
    values = [int(n) for n in f.read().split(',')]

# print len(values)

test = [1101,100,-1,4,0]

def run(nums):
    i = 0
    while True:
        sNum = str(nums[i])[-2:]
        pNum = str(nums[i])[:-2]
        if len(pNum) < 2: pNum = ("0" * (2 - len(pNum))) + pNum
        if '1' in sNum:
            st1, st2, st3 = nums[i+1], nums[i+2], nums[i+3]
            p1,p2 = 0,0
            p1 = st1 if pNum[1] is '1' else nums[st1]
            p2 = st2 if pNum[0] is '1' else nums[st2]
            nums[st3] = p1 + p2
            i += 4
        elif '2' in sNum:
            st1, st2, st3 = nums[i+1], nums[i+2], nums[i+3]
            p1,p2 = 0,0
            print "---------------"
            # print str(nums[i]) + "is nums[i]"
            print str(nums[i]) + "is opcode"
            print str(sNum) + " sNUm"
            print str(pNum[0]) + " 2nd pNUm " + str(pNum[1]) + " 1st pNUm"
            print str(st1) + " is st1"
            print str(nums[st1]) + " is nums[st1]"
            print str(st2) + " is st2"
            print str(nums[st2]) + " is nums[st2]"
            p1 = st1 if pNum[1] is '1' else nums[st1]
            p2 = st2 if pNum[0] is '1' else nums[st2]
            print str(p1) + " is p1"
            print str(p2) + " is p2"
            print str(nums[st3]) + " storing at st3: " + str(st3)
            nums[st3] = p1 * p2
            print str(nums[st3]) + " stored at st3: " + str(st3)
            i += 4
        elif '3' in sNum:
            nums[nums[i+1]] = 1
            i += 2
        elif '4' in sNum:
            #print str(nums[i + 1]) + " printed with opcode 4"
            i += 2
        elif '99' in sNum:
            break
        else:
            print "something wrong"
            break
    #if nums[0] == 19690720: print(100 * nums[1] + nums[2])
    # for i in range(len(nums)):
    #     print(values[i] - nums[i])

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