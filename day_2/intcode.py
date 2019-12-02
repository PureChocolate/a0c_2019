with open("input.txt", "r") as f:
    values = [int(n) for n in f.read().split(',')]

def run(nums):
    i = 0
    while True:
        st1, st2, st3 = nums[i+1], nums[i+2], nums[i+3]
        if nums[i] is 1: nums[st3] = nums[st1] + nums[st2]
        elif nums[i] is 2: nums[nums[i+3]] = nums[st1] * nums[st2]
        elif nums[i] is 99: break
        i += 4
    if nums[0] == 19690720: print(100 * nums[1] + nums[2])

for n1 in range(100):
    for n2 in range(100):
        num1 = values[:]
        num1[1] = n1
        num1[2] = n2
        run(num1)