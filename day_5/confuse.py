with open("in.txt", "r") as f:
    values = [int(n) for n in f.read().split(',')]

# print len(values)

test = [13,9,8,9,10,9,4,9,99,-1,8]

def run(nums):
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
            nums[nums[i+1]] = 5
            i += 2
        elif sNum == 4:
            print(str(nums[nums[i + 1]]) + " printed with opcode 4")
            i += 2
        # part 2 is 5/6/7/8 and input of 5 instead of 1 on code 3
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
run(values)
# fucking used nums[i+1] instead of nums[nums[i+1]] actual big brain (part 1)
# def run1(nums):
#     i = 0
#     while True:
#         sNum = str(nums[i])[-2:]
#         pNum = str(nums[i])[:-2]
#         if len(pNum) < 2: pNum = ("0" * (2 - len(pNum))) + pNum
#         if '1' in sNum:
#             st1, st2, st3 = nums[i+1], nums[i+2], nums[i+3]
#             p1,p2 = 0,0
#             p1 = st1 if pNum[1] is '1' else nums[st1]
#             p2 = st2 if pNum[0] is '1' else nums[st2]
#             nums[st3] = p1 + p2
#             i += 4
#         elif '2' in sNum:
#             st1, st2, st3 = nums[i+1], nums[i+2], nums[i+3]
#             p1,p2 = 0,0
#             p1 = st1 if pNum[1] is '1' else nums[st1]
#             p2 = st2 if pNum[0] is '1' else nums[st2]
#             nums[st3] = p1 * p2
#             i += 4
#         elif '3' in sNum:
#             nums[nums[i+1]] = 1
#             i += 2
#         elif '4' in sNum:
#             print(str(nums[nums[i + 1]]) + " printed with opcode 4")
#             i += 2
#         elif '99' in sNum:
#             break
#         else:
#             print "something wrong"
#             break

# run1(values)