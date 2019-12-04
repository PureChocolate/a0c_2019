from collections import Counter
start = 172851
end = 675869

def inc(input):
    track = int(input[0])
    for c in input:
        if int(c) < track:
            return False
        track = int(c)
    return True

def dub(temp):
    tc = Counter(temp)
    for x in tc:
        if tc[x] is 2:
            return True

count = 0
while(start < end):
    sStart = str(start)
    if dub(sStart) and inc(sStart):
        count += 1
    start += 1
print count

#len(set(sStart)) is not len(sStart)