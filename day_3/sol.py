with open("in.txt", "r") as f:
    lines = [str(x) for x in f.readlines()]
    a = lines[0].split(',')
    b = lines[1].split(',')

def run(line):
    cord = set()
    x,y = 0,0
    for move in line:
        if move[0] is "R": x += int(move[1:])
        elif move[0] is "L": x-= int(move[1:])
        elif move[0] is "U": y += int(move[1:])
        else: y -= int(move[1:])
        tup = (x,y)
        cord.add(tup)
    return cord
            

P1 = run(a)
if (995,0) in P1:
    print "woah"